def ganse(n):
    for i in range(n):
        yield i ** 2
        
for i in ganse(5):
    print(i)
    
print(sorted((x ** 3 for x in range(10)), reverse=True))

g = (x + 10 for x in range(5))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


l = 'spam'
for i in l:
    l = l[1:] + l[:1]
    print(l)
    
p = 'mans'
for i in range(len(p)):
    x = p[i:] + p[:i]
    print(x)
    
def tas(seq):
    return [seq[i:] + seq[:i] for i in range(len(seq))]

print(tas("likson"))