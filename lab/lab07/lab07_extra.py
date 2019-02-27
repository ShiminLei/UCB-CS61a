""" Optional Questions for Lab 07 """

from lab07 import *

# Q6
def remove_all(link, value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed. # 第一个 elem 永远不要remove

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    "*** YOUR CODE HERE ***"
    if link.rest == ():
        pass
    else:
        if link.rest.first == value:
            link.rest = link.rest.rest
            remove_all(link, value)
        else:
            remove_all(link.rest, value)



# Q7
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    if link == Link.empty:
        pass
    else:
        deep_map_mut(fn, link.rest)
        if isinstance(link.first, Link):
            deep_map_mut(fn, link.first)
        else:
            link.first = fn(link.first)

# Q8
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"


    def helper(link, have_seen=[]):
        #print(have_seen)
        if link is Link.empty:
            return False
        elif link in have_seen:
            return True
        else:
            have_seen.append(link)
            return helper(link.rest)  # 为什么这样也可以 return helper(link.rest)？这里传入的是当前的 have_seen

    return helper(link)

def has_cycle_constant(link): # 这个函数的 空间 是 O（1）
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return False

    slow, fast = link, link.rest

    while fast is not Link.empty:
        if fast.rest == Link.empty:
            return False
        elif fast is slow or fast.rest is slow: # 如果有环，快的就会追慢的，早晚有一天可以追上
            return True
        else:
            slow, fast = slow.rest, fast.rest.rest
    return False




# Q9
def reverse_other(t):
    """Mutates the tree such that nodes on every other (even_indexed) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    def helper(t, index = 1, label = None):

        length = len(t.branches)
        rev_labels = [t.branches[i].label for i in range(length - 1, -1, -1)]
        labels = [t.branches[i].label for i in range(length)]

        if index%2 == 1:
            i = 0
            for b in t.branches:
                helper(b, index+1, rev_labels[i])
                i+=1
        else: # 如果是偶数树
            t.label = label
            i = 0
            for b in t.branches:
                helper(b, index+1, labels[i])
                i+=1

    return helper(t)



