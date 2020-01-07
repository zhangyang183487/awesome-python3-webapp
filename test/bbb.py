# -*- coding: utf-8 -*-
import functools
from functools import reduce


def f(x, y=1):
    return x + y


L01 = [0, 2, 4, 6, 8]
L02 = (1, 3, 5, 7, 9)

ret1 = list(map(f, L01))
print(ret1)

ret2 = list(map(f, L01, L02))
print(ret2)

L03 = ret1 + ret2
print(L03)

print(reduce(f, L03))

print('=========================normalize=================================')


def normalize(name):
    if (name == None or len(name) == 0):
        raise TypeError('name is Empty.')

    name_new = None

    for i, v in enumerate(name):
        if (i == 0):
            name_new = v.upper()
        else:
            name_new = name_new + v.lower()

    return name_new;


nameList = {'rooney', 'kaka', 'messi'}

ret3 = map(normalize, nameList)
print(list(ret3))
print('=========================normalize=================================')

print('=========================prod=================================')


def prod(L):
    def myFuction(x, y):
        return x * y

    if (L == None or len(L) == 0):
        raise TypeError('List is Empty.')

    return reduce(myFuction, L)


print(prod(L02))

print('=========================prod=================================')

print('=========================filter=================================')


def doCompare(x):
    return x % 2 == 0;


print(list(filter(doCompare, L01)))
print(list(filter(doCompare, L02)))

print('=========================filter=================================')

print('=========================sorted=================================')
L03 = (11, 13, 5, 72, 9)
print(sorted(L03))
print(sorted(L03, key=abs, reverse=True))

print('=========================sorted=================================')

print('=========================count=================================')


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


L04 = count()
for i in L04:
    print(i());

print('=========================count=================================')

print('=========================createCounter=================================')


def createCounter():
    def doIncrease():
        n = 0;
        while True:
            n = n + 1;
            yield n;

    it = doIncrease();

    def counter():
        return next(it);

    return counter;


counterA = createCounter();
print(counterA(), counterA(), counterA());

print('=========================createCounter=================================')

print('=========================de111=================================')


# def logs2(text='execute2'):
def logs2(*text):
    def decorator(func):
        @functools.wraps(func)
        def info(*args, **kw):
            if text is None or len(text) == 0:
                print('%s():' % (func.__name__))
            else:
                print('%s %s():' % (text, func.__name__))
            print('begin call')
            func(*args, **kw);
            print('end call')
        return info;
    return decorator;


@logs2()
def today():
    print('2019-02-28');


# print(today.__name__)
print(today())

print('=========================de222=================================')


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
        print(n)
    return 'done'


print(list(fib(6)))

print()
print([x + x for x in L01])
print((x + x for x in L01))
myGen = (x + x for x in L01)
# print(next(myGen))
print()
for n in myGen: print(n)

print()


def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, range(1, 20)))
print(L)

print()
L2 = list(filter(lambda n: (n % 2 == 1), range(1, 20)))
print(L2)
