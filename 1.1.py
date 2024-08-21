import sys



s = 'sspam'
s = s.replace('s', 'x')
print(s)

i = 'xxxxSPAMxxxxSPAM'
print(i.replace('SPAM', 'EGGE', 2))

x = 1234
print('%e | %f | %g' % (x, x, x))
print('%-6.2f | %05.2f | %+06.1f' % (x, x, x))

reply = """
Greetings...
Hello %(name) s!
Your age is %(age) s
"""
value = {'name': 'Bob', 'age': 23}
print(reply % value)

template = '{0}, {1} and {2}'
print(template.format('spam', 'ham', 'eggs'))
template1 = '{motto}, {pork} and {food}'
print(template1.format(motto='spam', pork='ham', food='eggs'))
template2 = '{}, {} and {}'
print(template2.format('spam', 'ham', 'eggs'))

tap = '{mot}, {0} and {food}'.format(50, mot=3.14, food=[1, 2])
tap.split('and')
print(tap.replace('and', 'but under no circumstances'))

lapt = 'My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'})
print(lapt)

print('{0:10} = {1:10}'.format('spam', 123.4567))
print('{0:>10} = {1:>30}'.format('spam', 123.4567))
print('{0.platform:>10} = {1[kind]:>50}'.format(sys, dict(kind='laptop')))
print('{0:,d}'.format(999999999))
print('{dic} and {sap}'.format(dic='money', sap='bark'))
print('%(money)s and %(sap)s' % dict(money='mani', sap='peri'))
print('{0:f}, {1:.3f}, {2:05.2f}'.format(3.14159, 3.14159, 3.14159))