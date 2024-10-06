class tested():
    def __init__(self, state):
        self.state = state
    def nested(self, lable):
        print(lable, self.state)
        self.state += 1
        
a = tested(10)
print(a.nested('pint'))

def kend(start):
    def nefert(lable):
        print(lable, nefert.state)
        nefert.state += 1
    nefert.state = start
    return nefert

b = kend(100)
print(b('lol'))
print(b('dop'))