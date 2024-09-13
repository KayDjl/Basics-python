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