passphrase = 'CS61A'

def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    '3d2eea56786a3d9e503a4c07dd667867ef3d92bfccd68b2aa0900ead'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0, previous=None):
        self.value = value
        self.previous = previous

    def next(self):
        "*** YOUR CODE HERE ***"
        if self.previous == None:
            return Fib(1,self.copy())
        else:
            return Fib(self.value + self.previous.value, self.copy())

    def copy(self):
        return Fib(self.value, self.previous)

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15) #
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2) # 储存两颗糖
    'Current candy stock: 2'
    >>> v.vend() #取一颗糖
    'You must deposit $10 more.'
    >>> v.deposit(7) # 存7块钱
    'Current balance: $7'
    >>> v.vend() # 还需要3块才可以买糖
    'You must deposit $3 more.'
    >>> v.deposit(5) #再存5块钱
    'Current balance: $12'
    >>> v.vend() # 拿出一颗糖，找2块钱
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.stock = 0
        self.save = 0

    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        elif self.save < self.price:
            diff = self.price - self.save
            return 'You must deposit ${} more.'.format(diff)
        elif self.save == self.price:
            self.stock += -1
            self.save = 0
            return 'Here is your {}.'.format(self.name)
        else:
            self.stock += -1
            charge = self.save - self.price
            self.save = 0
            return 'Here is your {} and ${} change.'.format(self.name, charge)

    def deposit(self, money):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your ${}.'.format(money)
        else:
            self.save += money
            return 'Current balance: ${}'.format(self.save)

    def restock(self, num):
        self.stock += num
        return 'Current {} stock: {}'.format(self.name, self.stock)


