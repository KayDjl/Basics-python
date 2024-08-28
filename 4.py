import json

"""
myfile = open('textf.txt', 'w')
myfile.write('Hello world!\n')
myfile.write('Goodbye file\n')
myfile.close()
myfile = open('textf.txt')
print(myfile.read())
for line in myfile:
    print(line, end='')
"""
"""
x, y, z = 11, 22, 33
s = 'spam'
d = {'a': 1, 'b': 2}
v = [3, 4, 5]

myfile = open('textf1.txt', 'w')
myfile.write(s + '\n')
myfile.write('%s, %s, %s\n' % (x, y, z))
myfile.write(str(d) + '$' + str(v) + '\n')
myfile.close()
chars = open('textf1.txt')
line = chars.readline()
print(line)
line = chars.readline()
print(line)
line = chars.readline()
print(line)

chars = line.split('$')
print(chars)
kil = [eval(p) for p in chars]
print(kil)
"""

name = dict(first='bob', last='dev')
rec = dict(name=name, job=['meb', 'mgr'], age=40.5)
print(rec)
s = json.dumps(rec)
o = json.loads(s)
print(o == rec)

json.dump(rec, fp=open('jsonfile.txt', 'w'), indent=4)
print(open('jsonfile.txt').read())
