f = open("1.py")
print(f.__next__())

l = [1, 2, 3]
i = iter(l)
print(iter(i) is i)
print(next(i))
print(next(i))
print(next(i))
lines = f.readlines()
print(lines)
lin = [line.rstrip('\n') for line in lines]
print(lin)

x = range(5)
i1 = iter(x); i2 = iter(x)
print(i1.__next__(), i2.__next__())
print(i1.__next__(), i2.__next__())

v = [1, 2, 3]
r = map(abs, [1, 2, 3])
ll1 = iter(r); ll2 = iter(r)
print(ll1.__next__(), ll2.__next__())
print(ll1.__next__(), ll2.__next__())