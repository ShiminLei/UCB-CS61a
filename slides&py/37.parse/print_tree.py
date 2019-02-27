"""Pretty-print Trees as indented S-expressions."""

import heapq
import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

from tree import *
from io import StringIO

Leaf.__str__ = lambda leaf: '({tag} {word})'.format(**leaf.__dict__)

def print_tree(t, indent=0, end='\n'):
    """Print Tree or Leaf t with indentation.

    >>> np = Tree('NP', [Leaf('N', 'buffalo')])
    >>> t = Tree('S', [np, Tree('VP', [Leaf('V', 'buffalo'), np])])
    >>> print_tree(t)
    (S (NP (N buffalo))
       (VP (V buffalo)
           (NP (N buffalo))))
    """
    if isinstance(t, Leaf):
        print(t, end='')
    else:
        s = '(' + t.tag + ' '
        indent += len(s)
        print(s, end='')
        print_tree(t.branches[0], indent, '')
        for b in t.branches[1:]:
            print('\n' + ' '*indent, end='')
            print_tree(b, indent, '')
        print(')', end=end)

