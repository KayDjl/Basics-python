s = [1, 2, 3]
print(s + list('34'))
print(''.join([c*2 for c in 'spam']))
L = list(range(1, 75))
print (L)
L[len(L):] = [666, 777, 888]
print(L)
t = ['2', '4', '1', '9']
t.sort(reverse=True)
print(t)
print(sorted(t))
t.extend(['7', 5])
print(t)
t.pop()
print(t)
t.reverse()
print(t)
t = dict(one='y', two='b')
u = list(t.keys())
print(u)
c = []
for i in t.items():
    c.append(i)
print(c)
k = input('Bbb:' )
print(2 + int(k))
hech = {'pizz':'moriar', 'lacryni':'lenti', 'bachi':'hyri'}
print(hech['pizz'])
print([key for key in hech.keys() if hech[key] == 'hyri'])
print([key for (key, value) in hech.items() if value == 'lenti'])

matrix = {}
matrix[(2, 3, 6)] = 88
matrix[(1, 9, 4)] = 38
x = input()
x = int(x)
y = input()
y = int(y)
z = input()
z = int(z)
if (x, y, z) in matrix:
    print(matrix[(x, y, z)])
else:
    print(0)
    
d = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(d)

mid = list(range(1, 256))
di = {c: c**2 for c in mid}
print(di[186])

m = dict(li='1', ri='2')
ky = m.keys()
for i in sorted(ky):
    print(i, m[i])


