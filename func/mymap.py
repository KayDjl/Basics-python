def mymap(func, *seq):
    res = []
    for args in zip(*seq):
        res.append(func(*args))
    return res

print(mymap(pow, [1, 2, 3], [4, 5, 6]))

def myzip(*seq):
    seq = [list(s) for s in seq]
    res = []
    while all(seq):
        res.append(tuple(s.pop(0) for s in seq))
    return res

s1, s2 = 'snv', 'abc1'
print(myzip(s1, s2))