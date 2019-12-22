[TOC]
# cs61a

##  week 1

```python
from urllib.request import urlopen
shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')
```

#### 向下取整

The `//` operator, 向下取整

```
>>> 5 // 4
1
>>> -5 // 4
-2
```

These two operators are shorthand for the `truediv` and `floordiv` functions.

```python
>>> from operator import truediv, floordiv
>>> truediv(5, 4)
1.25
>>> floordiv(5, 4)
1
```
#### help 查看函数docstring

When you call `help` with the name of a function as an argument, you see its docstring . 

按住`q键`退出help

```python
>>> help(pressure)
```

## week 2 

####  Assertion

 `assert` statement 是布尔表达式，后面跟一句话。如果布尔表达式为False, 运行的时候会报错，停止运行，并显示这句话。

```python
>>> assert fib(8) == 13, 'The 8th Fibonacci number should be 13'
```

A test function for `fib` should test several arguments, including extreme values of `n`.

```python
>>> def fib_test():
        assert fib(2) == 1, 'The 2nd Fibonacci number should be 1'
        assert fib(3) == 1, 'The 3rd Fibonacci number should be 1'
        assert fib(50) == 7778742049, 'Error at the 50th Fibonacci number'
```

When writing Python in files, rather than directly into the interpreter, tests are typically written in the same file or a neighboring file with the suffix `_test.py`. （一般测试文件的命名方法，放在同一个文件夹下）

#### Doctests 

```python
>>> def sum_naturals(n):
        """Return the sum of the first n natural numbers.

        >>> sum_naturals(10)
        55
        >>> sum_naturals(100)
        5050
        """
        total, k = 0, 1
        while k <= n:
            total, k = total + k, k + 1
        return total
    
>>> from doctest import testmod
>>> testmod()
TestResults(failed=0, attempted=2)
```

```python
>>> from doctest import run_docstring_examples
>>> run_docstring_examples(sum_naturals, globals(), verbose=True)
#The second should always be the result of the expression `globals()`, a built-in function that returns the global environment.

Finding tests in NoName
Trying:
    sum_naturals(10)
Expecting:
    55
ok
Trying:
    sum_naturals(100)
Expecting:
    5050
ok
```

When writing Python in files, all doctests in a file can be run by starting Python with the doctest command line option:

```python
python3 -m doctest -v <python_source_file>
# 例子
python3 -m doctest -v lab01.py
```

#### False 值

   `0`, `None`, `''` (the empty string), and `[]` (the empty list) 

#### -i 交互界面

**-i**: The `-i` option runs your Python script, then opens an interactive session. In an interactive session, you run Python code line by line and get immediate feedback instead of running an entire file all at once.

```python
python3 -i lab01.py
```

#### lambda 表达式

```python
>>> compose1 = lambda f,g: lambda x: f(g(x))
```

#### decorators 装饰器函数

装饰器相当于一个高阶的函数

[装饰器解释视频]( https://www.bilibili.com/video/av25698102?from=search&seid=13362631726323047763)

```python
>>> def trace(fn):
        def wrapped(x):
            print('-> ', fn, '(', x, ')')
            return fn(x)
        return wrapped
    
>>> @trace
    def triple(x):
        return 3 * x
#相当于
>>> triple = trace(triple)
```

```python
# 第二个例子
>>> def display_time(func):
        def wrapper(*args):# 
            t1 = time.time()
            result = func()
            t2 = time.time()
            print("Total time: {:.4} s".format(t2 - t1))
            return result
        return wrapper    
    
>>> @display_time
	def triple(x):
        return 3 * x
```

## week 3 

#### multiple assignment

```python
def fib(n):
	'''
	Compute the nth fib number	
	>>> fib(0)
	0
	>>> fib(8)
	21
	'''
	k, kth, difference = 0, 0, 1
	while k<n:
		kth, difference = kth + difference, kth
		k+=1
	return kth
```

#### currying function

```python
def curry2(f):
	def g(x):
		def h(y):
			return f(x,y)
		return h
	return g

curry2 = lambda f: lambda x: lambda y: f(x,y)
#以上两个是等价的
```

```python
def horse(mask):
	horse = mask
	def mask(horse):
		return horse
	return horse(mask)

mask = lambda horse: horse(2) #lambda 传入的也可以是一个函数
horse(mask) # 答案是 2
```

#### print() 函数

```python
>>> a = print(1000) # print 函数只要被调用，就会有打印
1000

>>> a
>>>    #什么都不显示，因为 print 函数没有 return 
```

#### 递归函数

```python
>>> def cascade(n):
        """Print a cascade of prefixes of n."""
        if n < 10:
            print(n)
        else:
            print(n)
            cascade(n//10)
            print(n)
>>> cascade(2013)
2013
201
20
2
20
201
2013
```

## week 4

#### 最大公约数

```python
from fractions import gcd
>>> gcd(2,8)
2
```

#### print(None)

```python
>>> a = None
>>> print(a)
None
>>> a
>>> # 什么都不显示
```

## week 5

#### exec 执行字符串里面的命令

```python
>>> exec('print(1)')
1
```

#### in 在string匹配subsequence

```python
>>> 'here' in 'where is the dog'
True
>>> [1,2,3] in [1,2,3,4,5]
False

# in 在 string 里面可以匹配 subsequence
```

#### dic.get(key, 默认值)

默认值指的是，如果key不存在，则返回这个默认值

#### dic comprehension

```python
{x:x*x for x in range(10)}
```

#### sum 的妙用

```python
def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    "*** YOUR CODE HERE ***"
    if type(lst) != list:
        return [lst]
    else:
        return sum([flatten(elem) for elem in lst],[])

>>> [1]+[1,2]
[1,1,2]
```

#### 重要技巧～！用列表推导式复制，形成多维列表

```python
table = [[1,1]]*2 
print(table) # [[1, 1], [1, 1]]
table[0][0]=9
print(table) # [[9, 1], [9, 1]]
#用 is 查是不是一个对象，发现每行其实是一个对象
print( table[0][0] is table[1][0] ) # True
# 这样的话改一个数字，相应位置都会改，因为每个行的指针都指向一个地方
[[1, 1], [1, 1]]
[[9, 1], [9, 1]]
True

#但是如果这样,相当于用循环赋值，就可以
table = [[1,1] for _ in range(2)]
print(table)
table[0][0]=9
print(table)
print( table[0][0] is table[1][0] )

[[1, 1], [1, 1]]
[[9, 1], [1, 1]]
False
```

总之不要轻易使用 list*size，因为会存在指针问题。

## week 6

#### Non-local Assignment

```python
def make_withdraw(balance):
    '''
    Return a withdraw function with a starting balance.
    '''
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw
withdraw = make_withdraw(100)
withdraw(10) #90
withdraw(10) # 80
```

#### object  attribute

```python
>>> getattr(tom_account, 'balance')
10
>>> hasattr(tom_account, 'balance')
True
```

#### copy tree 用函数实现

```python
def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])
```

#### random.choice(list)

to randomly select from a list, import the Python random library with `import random` and use the expression `random.choice(my_list)`)

#### Attributes

```python
class Car(object):
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color
    

```

#### method

```python
>>> hilfingers_car.paint('black')
'Tesla Model S is now black'
>>> hilfingers_car.color
'black'

# 重点！！！上述method等效于
>>> Car.paint(hilfingers_car, 'red')
'Tesla Model S is now red'
```

## week 7

#### 多类继承
![image](http://note.youdao.com/yws/res/2105/67057ECDDCB3453482BF156186D74837)
For a simple "diamond" shape like this, Python resolves names from left to right, then upwards. 这个例子中按照从下到上，从左到右的顺序继承

```
AsSeenOnTVAccount, CheckingAccount, SavingsAccount, Account, object
```

但是实际上，对于复杂类的继承顺序并不是这么简单。理论是按照 C3 Method Resolution Ordering 的顺序。

The method resolution order of any class can be queried using the `mro` method on all classes.

```python
>>> [c.__name__ for c in AsSeenOnTVAccount.mro()]
['AsSeenOnTVAccount', 'CheckingAccount', 'SavingsAccount', 'Account', 'object']
```

The precise algorithm for finding method resolution orderings is not a topic for this text, but is [described by Python's primary author](http://python-history.blogspot.com/2010/06/method-resolution-order.html) with a reference to the original paper.

#### String Representation: repr str

In Python, 所有对象有两种string表达方式：

**str** is legible to human.

**repr** is legible to Python Interpreter.出现的就是在交互界面上的内容

```python
eval(repr(object)) == object

>>> 12e12
12000000000000.0
>>> repr(12e12)
'12000000000000.0'
>>> print(repr(12e12))
12000000000000.0

>>> min
<built-in function min>
>>> repr(min)
'<built-in function min>'

>>> from fractions import Fraction
>>> half = Fraction(1,2)
>>> repr(half)
'Fraction(1, 2)'
>>> str(half)  #人类可读的
'1/2'
>>> print(half) # print出来的内容，是str的内容
1/2
```

#### polymorphic function 多态函数

```python
def repr(x): # class 传入
    return type(x).__repr__(x)    
```

#### 特殊内置method

两边带双下划线的函数名，一般是python build-in function。

```python
# -*- coding: UTF-8 -*-

class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({0},{1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer,self.denom)

    def __add__(self, other):
        if isinstance(other, int): # 判断是不是一类
            n = self.numer + self.denom * other
            d = self.denom
        elif isinstance(other, Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        elif isinstance(other, float):
            return float(self) + other
        g = gcd(n, d)
        return Ratio(n//g, d//g)

    __radd__ = __add__ ##radd - right side addition: 就是加号左右两边交换位置也可以运算

    def __float__(self):
        return self.numer/self.denom

def gcd(n,d):
    while n!= d:
        n,d = min(n,d),abs(n-d)
        return n

    
>>> Ratio(1,2)+1
Ratio(1,1)
>>> 1+Ratio(1,2)
Ratio(1,1)
>>> 0.2 + Ratio(1,3)
0.5333333333333333
```

#### measuring efficiency

```python
def count(f):
    def counted(n):
        counted.call_count+=1
        return f(n)
    counted.call_count = 0 # 每次 fib = count(fib) 赋值一次，清零
    return counted


def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-2) + fib(n-1)
>>> fib(30)
832040
>>> fib.call_count
2692537 #你发现这个数字非常大

```

#### Memoization

记住之前计算的值

```python
>>> fib = memo(fib)
>>> fib = count(fib)
>>> fib(30)
832040
>>> fib.call_count
59  # 这个值会变得非常小

```

## week 8 (开始讲数据结构)

#### Link List (装饰器让method不带括号）

```python
class Link():
    empty = ()
    def __init__(self,first,rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    @property  # 这个装饰器可以让 method 调用不带（）
    def second(self):
        return self.rest.first

    @second.setter # .setter 是一种特定的装饰器, 可以用 = 直接赋值，而不用调用其他的方法
    def second(self,value):
        self.rest.first = value

    def __repr__(self): # 这个是在交互界面上展示的形式
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self): # 这个是在<1 2 3> 类似这样的表现形式
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i - 1]

    def __len__(self):
        return 1 + len(self.rest) # ()的长度是 0
    
    def __add__(s, t):  # 实现两个 link 的拼接
        if s is Link.empty:
            return t
        else:
            return Link(s.first, Link.__add__(s.rest, t))

>>> a = Link(1,Link(2))
>>> a
Link(1, Link(2)) #交互界面展示的形式，由__repr__函数决定
>>> str(a)
'<1 2>'   # 由 __str__ 函数决定
>>> a.second # 装饰器 @property 的作用
2

>>> a.second = 9 #以下是 .setter 的作用
>>> a.second
9
>>> a
Link(1, Link(9))
```

```python
def map_link(f, s): # 相当于 map 对列表的作用，把一个函数 f 作用到每一个节点上
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s): # 这里的 f 的输出是 bool,用来判断属性的
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered

def join_link(s, separator): # 用 separator 的符号连接 link中的每个数字
    if s is Link.empty:
        return ""
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + separator + join_link(s.rest, separator)
```



#### Tree

```python

class Tree:
    def __init__(self,label,branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches) # list 这里是为了让 tuple 也可以

    def __repr__(self):
        if self.branches:
            branches_str = ', '+repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str)

    def is_leaf(self):
        return not self.branches

    def __eq__(self, other):  # == 等于符号的build-in 函数
        return type(self) is type(other) \
                and self.label == other.label \
                and self.branches == other.branches

    def __str__(self):  # 这个主要用来 print tree, 可以出来有结构的tree
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip() # 用于删除最后的 \n

    def copy_tree(self):
        return Tree(self.label, [b.copy_tree() for b in self.branches])

>>> a = Tree(1, [Tree(1)])
>>> a
Tree(1, [Tree(1)])
>>> str(a)
'1\n  1'
>>> print(a)
1
  1

```

#### link 的循环～～！重点

```python
>>> link = Link(1)
>>> link.rest = link
>>> link.rest.rest.rest.rest.first
1
# 是1 的原因是，把link的rest指向link自己的头，这样会循环自己
```

#### 检查Link是否有循环, 快慢双指针

```python
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

```

## week 9

#### lists in lists in lists 环境图
![image](http://note.youdao.com/yws/res/1904/3F2B4737FAF84EA988B6DC60F27C6600)

list.extend 其实是指针指到另一个数组。

## week 10 (Scheme)

#### Exception 异常报错

assertion 可以在python里面不执行，如果用 `python3 -O` . 这里是大写 O.

```python
assert False, 'error'
# 用python -O .py 执行不会报错
```

#### Try - except

```python
def invert(x):
    y = 1/x
    print('Never printed if x is 0')
    return y

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print('handled',e)
        return 0
    
>>> invert_safe(0)
handled division by zero
0
>>> invert_safe(2)
Never printed if x is 0
0.5
```

#### reduce

```python
from operator import add,mul
def reduce(f,s,initial):
    '''
    >>> reduce(mul, [2,4,8],1)
    64
    >>> reduce(add, [1,2,3,4],0)
    10
    '''
    for x in s:
        initial = f(initial, x)
    return initial
```

#### lab09

To start the interpreter, type `python3 scheme`. To run a Scheme program interactively, type `python3 scheme -i <file.scm>`. To exit the Scheme interpreter, type `(exit)`.



## week 12 (Interpreter)



## week 13 (Iterators)

#### Interators

可以把iterator看成一种position

```python
>>> s = [3,4,5]
>>> t = iter(s)
>>> next(t)
3
>>> next(t)
4
>>> next(t)
5

>>> next(u)
3
# 也就是说，t,u 互不影响，只是代表一个position
```

#### 设计 contains('strength', 'stent')

```python
def contains(a, b):
    ai = iter(a)
    for x in b:
        try:
            while next(ai) != x:
                pass # do nothing
        except StopIteration:
            return False
    return True

>>> contains('strength', 'stent')
True # 第二个单词按顺序包含在第一个单词里面
```

#### Built-in Functions for Iteration

```python
map(func, iterable) # 得到的是 iter
filter(func, iterable)
zip(first_iter, second_iter)
reversed(sequence)

list(iterable)
tuple(iterable)
sorted(iterable)
```

滞后执行：func 不是立刻在iter的每个元素上执行，而是到哪里，就执行到哪里。

#### Generator

```python
def plus_minus(x):
    yield x
    yield -x
>>> t = plus_minus(x)
>>> next(t)
3
>>> next(t)
-3
```

normal function 只能return一次，但是 generator function可以yield很多次。

```python
def a_then_b(a, b):
    for x in a:
        yield x
    for x in b:
        yield x
# 下面和上面等价
def a_then_b(a, b):
    yield from a
    yield from b
    
>>> list(a_then_b([3,4],[5,6]))
[3,4,5,6]
```

#### raise Error

```python
def trap(s, k): # 产生前 k 个值
    """Return a generator that yields the first K values in iterable S,
    but raises a ValueError exception if any more values are requested.

    >>> t = trap([3, 2, 1], 2)
    >>> next(t)
    3
    >>> next(t)
    2
    >>> next(t)
    ValueError
    >>> list(trap(range(5), 5))
    ValueError
    >>> t2 = trap(map(abs, reversed(range(-6, -4))), 2)
    >>> next(t2)
    5
    >>> next(t2)
    6
    >>> next(t2)
    ValueError
    """
    "*** YOUR CODE HERE ***"
    assert len(s) >= k
    counter = 0
    iterator = iter(s)
    while counter < k:
        yield next(iterator)
        counter += 1
    raise ValueError
```



## week 14

#### SQL （Declarative Programming）

```sql
create table [name] as [select statement]#指的是下面的
    select expression as name, expression as name union
    select expression        , expression         union

例子：
create table parents as 
	select 'a' as parent, 'aa' as child union
	select 'b'          , 'bb'          union
	

select [columns] from [table] where [condition] order by [order]
例子：
select child from parents where parent = 'a'

```











































