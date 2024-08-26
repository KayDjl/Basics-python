from collections import namedtuple



mun = ('aa', 'vv', 'bb', 'rr')

tmp = list(mun)
tmp.sort()
print(tmp)

t = tuple(tmp)
print(sorted(t))
print([x for x in t])

rec = namedtuple('Rec', ['name', 'age', 'jobs'])
bob = rec('Bob', age=21, jobs=['mrg', 'dev'])

print(bob)
print(bob.name, bob.jobs)
print([bob[0], bob[1], bob[2]])
o = bob._asdict()
print(o)
print(o['age'], o['jobs'])