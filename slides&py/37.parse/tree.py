class Tree:
    def __init__(self, tag, branches):
        assert len(branches) >= 1
        for b in branches:
            assert isinstance(b, (Tree, Leaf))
        self.tag = tag
        self.branches = branches

class Leaf:
    def __init__(self, tag, word):
        self.tag = tag
        self.word = word

beasts =     Leaf('N', 'buffalo')
intimidate = Leaf('V', 'buffalo')
S, NP, VP =  'S', 'NP', 'VP'

s = Tree(S, [Tree(NP, [beasts]),
             Tree(VP, [intimidate,
                       Tree(NP, [beasts])])])
