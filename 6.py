#coding: utf-8
choice = 'pet'
#Аналог switch\case
"""
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

by = input("Number: ")
mt = int(by) // 2
while mt > 1:
    if int(by) % mt == 0:
        print(by, "somnosgetel", mt)
        break
    mt -= 1
else:
    print(by, "easy")
"""
for ((a, b), c) in (([1, 2], 4), ['MY', 1], ((6, 7), [7])):
    print(a, b, c)
   
file = open('jsonfile.txt', 'r')
while True:
    char = file.read(10)
    if not char:
        break
    print(char)
        
for char in open('jsonfile.txt').readlines():
    print(char.rstrip())