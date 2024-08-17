s = '0123456789'
print(s[::3])
x = 'hello'
print(x[::-1])
print(int('42') + 1)
print('spam', repr('spam'))
print(ord('s'))
print(chr(115))
print([ord(x) for x in "spam"])
print(ord('5') - ord('0'))

b = '100'
i = 0
while b != '':
    i = i * 2 +(ord(b[0]) - ord('0'))
    b = b[1:]
print(i, bin(i))
x = [x for x in 'spam']
x[0] = 'x'
print(''.join(x))
s = 'spam'
s = s + 'SPAM!'
s = s[:4] + 'Burger' + s[-1]
print(s)
l = 'Leter'
print(l.replace('et', 'yr'))
print('That is %d %s bird' % (1, 'dead'))
print('That is {0} {1} bird'.format(1, 'dead'))
s, a = 1, 'dead'
print(f"That is {s} {a} bird")