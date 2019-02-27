""" Optional problems for Lab 6 """

## Nonlocal practice
def vending_machine(snacks):
    """Cycles through sequence of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',))
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    count = 0
    "*** YOUR CODE HERE ***"
    def helper():
        nonlocal count
        #nonlocal snacks
        now = count % len(snacks)
        count += 1
        return snacks[now]
    return helper