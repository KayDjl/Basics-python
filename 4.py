import json
import struct


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
"""
name = dict(first='bob', last='dev')
rec = dict(name=name, job=['meb', 'mgr'], age=40.5)
print(rec)
s = json.dumps(rec)
o = json.loads(s)
print(o == rec)

json.dump(rec, fp=open('jsonfile.txt', 'w'), indent=4)
print(open('jsonfile.txt').read())
"""
"""
myfl = open('bytefile.bin', 'wb')
data = struct.pack('>i4sh', 7, b'spam', 8)
print(data)
myfl.write(data)
myfl.close()
f = open('bytefile.bin', 'rb')
data1 = f.read()
print(data)
values = struct.unpack('>i4sh', data1)
print(values)
"""
A = [1, 2, 3]
B = {'a': 4, 'b': 4}
L = [10, A, 84]
D = {'x':B, 'y':14}
A[1] = 'br'
print("{}\n{}\n{}\n{}\n".format(A, B, L, D))
N = list(A)
M = B.copy()
N[1] = 'Ni'
M['col'] = 'lenti'
print("{}\n{}\n{}\n{}\n".format(A, B, N, M))

pin = 'a sssssppppppaaaaaammmmmm preee a lot longer string'
din = 'a sssssppppppaaaaaammmmmm preee a lot longer string'
print(pin == din, pin is din)

pin = [1, 2, 4]
din = [1, 2, 3]
print(pin == din, pin is din)