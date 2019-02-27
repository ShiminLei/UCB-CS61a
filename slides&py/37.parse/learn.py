"""Count words and rules from a Treebank."""

from collections import Counter, defaultdict
from tree import Tree, Leaf

import pickle
import sys

class Tokenizer:
    """An iterator over the tokens of a Treebank."""
    def __init__(self, input):
        self.input = input
        self.line = []

    def __next__(self):
        """Return the next token."""
        while self.line == []:
            s = self.input.readline()
            if s == '':
                raise StopIteration
            self.line = s.replace('(', ' ( ').replace(')', ' ) ').split()
        return self.line.pop(0)

def read_trees(input):
    """Yield trees in a file."""
    tokens = Tokenizer(input)
    while True:
        assert next(tokens) == '('
        assert next(tokens) == '('
        tree = read_tree(tokens)
        if tree:
            yield tree
        assert next(tokens) == ')'

def read_tree(tokens):
    """Read the next well-formed tree, removing empty constituents."""
    tag = next(tokens).split('-')[0].split('=')[0].split('|')[0]
    element = next(tokens)
    if element != '(':
        assert next(tokens) == ')'
        return Leaf(tag, element)
    branches = []
    while element != ')':
        assert element == '('
        branch = read_tree(tokens)
        if branch and branch.tag:
            branches.append(branch)
        element = next(tokens)
    if branches:
        return Tree(tag, branches)

def gen_rules(tree):
    """Yield rules of a tree as (tag, tags) pairs, collapsing unary chains."""
    if tree.tag and isinstance(tree, Tree):
        branches = tree.branches
        while len(branches) == 1 and isinstance(branches[0], Tree):
            branches = branches[0].branches
        if branches:
            yield tree.tag, tuple(b.tag for b in branches)
        for branch in branches:
            for rule in gen_rules(branch):
                yield rule

def gen_words(tree):
    """Yield the leaves of a tree."""
    if tree.tag:
        if isinstance(tree, Tree):
            for b in tree.branches:
                for leaf in gen_words(b):
                    yield leaf
        else:
            yield tree

def estimate(path='model.p', rules_per_tag=100, tags_per_word=5):
    """Estimate and output normalized grammar and lexicon parameters."""
    grammar = defaultdict(Counter) # grammar[tag][child_tags] -> count
    words = defaultdict(Counter)   # words[tag][word] -> count
    for tree in read_trees(sys.stdin):
        for tag, tags in gen_rules(tree):
            grammar[tag][tags] += 1
        for leaf in gen_words(tree):
            words[leaf.tag][leaf.word] += 1

    # Normalize grammar
    for tag, tags in grammar.items():
        total = sum(tags.values())
        grammar[tag] = {k: v/total for k, v in tags.most_common(rules_per_tag)}

    # Normalize and invert words
    lexicon = defaultdict(Counter) # lexicon[word][tag] -> frequency
    for tag, words in words.items():
        total = sum(words.values())
        for word, count in words.items():
            lexicon[word][tag] = count/total
    for word, tags in lexicon.items():
        lexicon[word] = dict(tags.most_common(tags_per_word))

    with open(path, 'wb') as out:
        pickle.dump({'grammar': grammar, 'lexicon': lexicon}, out)

if __name__ == '__main__':
    estimate()

