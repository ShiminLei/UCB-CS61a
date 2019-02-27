""" Optional Questions for Lab 11 """

from lab11 import *

# Q5
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    yield n
    while n!=1:
        if n%2 == 0:
            n = n//2
        elif n%2 == 1:
            n = n*3+1
        yield n

# Q6
def repeated(t, k):
    """Return the first value in iterable T that appears K times in a row. 指的是连续出现 k 次

    >>> s = [3, 2, 1, 2, 1, 4, 4, 5, 5, 5]
    >>> repeated(trap(s, 7), 2)
    4
    >>> repeated(trap(s, 10), 3)
    5
    >>> print(repeated([4, None, None, None], 3))
    None
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    iterator = iter(t)
    prev = next(iterator)
    counter = 1
    for val in iterator:
        if val == prev:
            counter += 1
            if counter == k:
                return val
        else:
            counter = 1
        prev = val
    return "No value appears K times in a row"


# Q7
def merge(s0, s1):
    """Yield the elements of strictly increasing iterables s0 and s1, removing
    repeats. Assume that s0 and s1 have no repeats. s0 or s1 may be infinite
    sequences.

    >>> m = merge([0, 2, 4, 6, 8, 10, 12, 14], [0, 3, 6, 9, 12, 15])
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    >>> def big(n):
    ...    k = 0
    ...    while True: yield k; k += n
    >>> m = merge(big(2), big(3))
    >>> [next(m) for _ in range(11)]
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    i0, i1 = iter(s0), iter(s1)
    e0, e1 = next(i0, None), next(i1, None) # 这里这个None的意思是，如果到最后出现StopIteration,则以None代替
    "*** YOUR CODE HERE ***"
    while (e0 is not None) or (e1 is not None):
        if e0 is None:
            yield e1
            e1 = next(i1, None)
        elif e1 is None:
            yield e0
            e0 = next(i0, None)
        elif e0 == e1:
            yield e0
            e0, e1 = next(i0, None), next(i1, None)
        elif e0 < e1:
            yield e0
            e0 = next(i0, None)
        elif e0 > e1:
            yield e1
            e1 = next(i1, None)



# Q8
def remainders_generator(m):
    """
    Takes in an integer m, and yields m different remainder groups
    of m.

    >>> remainders_mod_four = remainders_generator(4)
    >>> for rem_group in remainders_mod_four:
    ...     for _ in range(3):
    ...         print(next(rem_group))
    0
    4
    8
    1
    5
    9
    2
    6
    10
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"
    def helper(num, m):
        while True:
            yield num
            num += m
    for num in range(m):
        yield helper(num, m)

# Q9
def zip_generator(*iterables):
    """
    Takes in any number of iterables and zips them together.
    Returns a generator that outputs a series of lists, each
    containing the nth items of each iterable.
    >>> z = zip_generator([1, 2, 3], [4, 5, 6], [7, 8])
    >>> for i in z:
    ...     print(i)
    ...
    [1, 4, 7]
    [2, 5, 8]
    """
    "*** YOUR CODE HERE ***"
    iterator = iter(zip(*iterables))
    for _ in range(len(list(zip(*iterables)))):
        yield list(next(iterator))
