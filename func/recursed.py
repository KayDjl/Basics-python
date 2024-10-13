def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])
    
x = mysum([1, 2, 3, 4, 5])
print(x)

def mysum1(L):
    return 0 if not L else L[0] + mysum1(L[1:])

def mysum2(L):
    return L[0] if len(L) == 1 else L[0] + mysum2(L[1:])

def mysum3(L):
    first, *rest = L
    return first if not rest else first + mysum3(rest)

x1 = mysum1([1, 3, 5, 7, 9])
x2 = mysum2(['s', 'p', 'a', 'm'])
x3 = mysum3(['spam', 'eggs', 'wow'])

print("{}\n{}\n{}".format(x1, x2, x3))

def glmysum(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += glmysum(x)
    return tot
        
x4 = glmysum([1, 2, 3, [4, 5, [6, 7]], 8, 9])
print(x4)
