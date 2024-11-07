import sys, timeit

print(sys.version)
print(min(timeit.repeat(stmt="[x ** 2 for x in range(1000)]", number=1000, repeat=5)))

print(timeit.repeat(stmt="list(map(lambda x: x ** 2, range(1000)))", number=1000, repeat=5))

