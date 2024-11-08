import sys, timeit
from functools import reduce
from math import factorial

def rec1(x):

    if x > 0:
        return x * rec1(x - 1)
    else:
        return 1

print(rec1(10))

def rec2(x):
    return reduce(lambda a, b: a * b, range(1, x + 1)) 

print(rec2(5))

def rec3(x):
    fac = 1
    for i in range(1, x + 1):
        fac *= i
    return fac

print(rec3(15))

def rec4(x):
    return factorial(x)

print(rec4(5))

def test_rec1():
    return timeit.timeit("rec1(10)", setup="from __main__ import rec1", number=1000)

def test_rec2():
    return timeit.timeit("rec2(10)", setup="from __main__ import rec2", number=1000)

def test_rec3():
    return timeit.timeit("rec3(10)", setup="from __main__ import rec3", number=1000)

def test_rec4():
    return timeit.timeit("rec4(10)", setup="from __main__ import rec4", number=1000)

print("Recursed = %s" % (test_rec1()))
print("Reduce = %s" % (test_rec2()))
print("For = %s" % (test_rec3()))
print("Factorial() = %s" % (test_rec4()))


