#coding: utf-8
choice = 'pet'
#Аналог switch\case
print({"yert": 1.22,
       "peri": 183,
       "pet": 1.77,
       "uli": 99} [choice])

bec = {'spam': 1,
       'len': 2,
       'ter': 3}
print(bec.get('spam', 'Bad choice'))
print(bec.get('heri', 'Bad choice'))

print(2 or 3, [] or 3, {} or [])
print(2 and 3, [] and 3, {} and [])
x = 1
y = 0
z = 3
m = y if x else z
print(m)
a = ((x and y) or z)
print(a)
if x and y:
    print(1)
else:
    print(2)