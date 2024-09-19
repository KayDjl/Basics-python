import sys
a = ''
b = 0
print([x for x in dir(a) if not x.startswith('__')])
print(sys.__doc__)
p = map(lambda t: t ** 2, range(7))
print(list(p))