#coding: utf-8
import os
from uu import encode

x = 'spam'
for item in x:
    print(item, end=' ')

i = 0
while i < len(x):
    print( x[i], end=' ')
    i += 1
    
for i in range(len(x)):
    x = x[1:] + x[:1]
    print(x, end=' ')
    

for i in range(0, len(x), 2):print(x[i], end=' ')

l1 = list(range(0, 10))
l2 = list(range(0, 100, 10))
zp = list(zip(l1, l2))
for (x, y) in zp:
    print(x, y, "--", x + y)
    
k1 = [1, 2, 3, 4 ,5]
k2 = [6, 7, 8, 9, 10, 11, 12]
zp1 = list(zip(k1, k2))
print(zp1)
d = dict(zip(k1, k2))
print(d)

for i in os.popen('systeminfo'):print(i.rstrip())

for i in 'spam':
    print(i, end='')
else:
    print('\nEnd')
    
