from tree import Tree, Leaf
from print_tree import print_tree

lexicon = {
        Leaf('N', 'buffalo'), # beasts
        Leaf('V', 'buffalo'), # intimidate
        }

grammar = {
        'S':  [['NP', 'VP']],
        'NP': [['N']],
        'VP': [['V', 'NP']],
        }

def expand(tag):
    """Yield all trees rooted by tag."""

def expand_all(tags):
    """Yield all sequences of branches for a sequence of tags."""
