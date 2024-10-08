def f(a):
    a = 99
b = 88
f(b)
print(b)

def changer(a, b):
    a = 2
    b = b[:]
    b[0] = 'spam'
    return a, b
    
x = 1
l = [1, 2]
print(changer(x, l))
print(x, l)
