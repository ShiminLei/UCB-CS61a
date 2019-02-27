import heapq, math, pickle
from tree import Tree, Leaf
from print_tree import print_tree

model = pickle.load(open('model.p', 'rb'))
grammar = model['grammar'] # grammar[tag][tags] -> frequency
lexicon = model['lexicon'] # lexicon[word][tag] -> frequency

def max_parses(line, n=1):
    words = line.split()

    @memoize
    @max_trees(n)
    def expand(start, end, tag):
        """Yield all trees rooted by tag over words[start:end]."""
        if end-start == 1:
            word = words[start]
            if tag in tags_for_word(word):
                yield Leaf(tag, word)
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

def tags_for_word(word):
    """Return tags for word, providing open-class options for unknown words."""
    if word in lexicon:
        return lexicon[word].keys()
    else:
        return ('JJ', 'NN', 'VB')

def memoize(f):
    """Decorator to memoize function f of immutable arguments."""
    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoized

def max_trees(n):
    """Decorator to return maximal scoring trees from a function f."""
    def max_from(f):
        def maxed(*args):
            return heapq.nlargest(n, f(*args), key=score)
        return maxed
    return max_from

@memoize
def score(t, unknown_word_frequency=1e-5):
    """Score Tree or Leaf t as the sum of grammar/lexicon log frequencies."""
    if isinstance(t, Tree):
        tags = tuple(b.tag for b in t.branches)
        rule_score = math.log(grammar[t.tag][tags])
        return rule_score + sum(score(b) for b in t.branches)
    else:
        word, tag = t.word, t.tag
        return math.log(lexicon.get(word, {}).get(tag, unknown_word_frequency))

def top10(m):
    """Return the top 10 keys from a dict ordered by their values."""
    return heapq.nlargest(10, m.keys(), key=m.get)
