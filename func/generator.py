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
print(next(g))
print(next(g))