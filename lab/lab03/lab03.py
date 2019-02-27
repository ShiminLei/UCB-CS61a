""" Lab 3: Recursion and Midterm Review """

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    a,b = max(a,b), min(a,b)

    if a%b!=0: 
        return gcd(b, a%b)
    else:
        return b



def hailstone(n, count=1):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    print(n)
    
    if n==1:
        return count
    elif n%2==0:
        return hailstone(n//2, count+1)
    else:
        return hailstone(n*3+1, count+1)



