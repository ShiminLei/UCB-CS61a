from tree import Tree, Leaf
from print_tree import print_tree

lexicon = {
        Leaf('N', 'buffalo'), # bison
        Leaf('V', 'buffalo'), # intimidate
        Leaf('J', 'buffalo'), # New York
        Leaf('R', 'that'),
        }

grammar = {
        'S':  [['NP', 'VP']],
        'NP': [['N'], ['J', 'N'], ['NP', 'RP']],
        'VP': [['V', 'NP']],
        'RP': [['R', 'NP', 'V'], ['NP', 'V']],
        }

def expand(tag):
    """Yield all trees rooted by tag."""
    for leaf in lexicon:
        if leaf.tag == tag:
            yield leaf
    if tag in grammar:
        for tags in grammar[tag]:
            for branches in expand_all(tags):
                yield Tree(tag, branches)

def expand_all(tags):
    """Yield all sequences of branches for a sequence of tags."""
    if len(tags) == 1:
        for branch in expand(tags[0]):
            yield [branch]
    else:
        first, rest = tags[0], tags[1:]
        for first_branch in expand(first):
            for rest_branches in expand_all(rest):
                yield [first_branch] + rest_branches

def parse(line):
    words = line.split()

    def expand(start, end, tag):
        """Yield all trees rooted by tag over words[start:end]."""
        if end-start == 1:
            word = words[start]
            for leaf in lexicon:
                if leaf.tag == tag and leaf.word == word:
                    yield leaf
        if tag in grammar:
            for tags in grammar[tag]:
                for branches in expand_all(start, end, tags):
                    yield Tree(tag, branches)

    def expand_all(start, end, tags):
        """Yield all sequences of branches for tags over words[start:end]."""
        if len(tags) == 1:
            for branch in expand(start, end, tags[0]):
                yield [branch]
        else:
            first, rest = tags[0], tags[1:]
            for middle in range(start+1, end+1-len(rest)):
                for first_branch in expand(start, middle, first):
                    for rest_branches in expand_all(middle, end, rest):
                        yield [first_branch] + rest_branches

    for tree in expand(0, len(words), 'S'):
        print_tree(tree)
