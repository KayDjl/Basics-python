def f(a):
    a = 99
b = 88
f(b)
print(b)

def changer(a, b):
    a = 2
    b = b[:]
    b[0] = 'spam'
    return a, b
    
x = 1
l = [1, 2]
print(changer(x, l))
print(x, l)

def cool(a, b, c=3): print(a, b, c)    

cool(1, b=8, c=10)

def p(*args): print(args)

p(1, 2, 3, 'end')

def pop(a, *args, **kargs): print(a, args, kargs)

pop(10, 11, 12, di='men', pi=3.14)

def kpop(a, *, c=3, b='do'): print(a, c, b)
kpop(11, b=123)

def mins(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]
print(mins(2, 5, 4, 121, 1, 9))

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res
def less(x, y): return x < y
def grtr(x, y): return x > y

print(minmax(less, 4, 12, 21, 10))
print(minmax(grtr, 182, 11, 10, 21))
