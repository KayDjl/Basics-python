def instens(seq1, seq2):
    res = []
    for i in seq1:
        if i in seq2:
            res.append(i)
    return res

x = 'spamM'
p = 'sram'
print(instens(x, p))

m = 100
def loc1():
    m = 110
    def loc2():
        print(x)
    loc2()
loc1()

def mark(n):
    def act(x):
        return x ** n
    return act
meb = mark(10)
print(meb(2))