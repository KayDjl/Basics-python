s = [1, 2, 3]
print(s + list('34'))
print(''.join([c*2 for c in 'spam']))
L = list(range(1, 75))
print (L)
L[len(L):] = [666, 777, 888]
print(L)