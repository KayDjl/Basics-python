def echo(message):
    print(message)
    
echo("Hello")
x = echo
x("world!")

def inderect(func, arg):
    func(arg)
   
inderect(x, "Hello world")

slep = [(x, "Spam"), (x, "Ham")]
for (func, arg) in slep:
    func(arg)
    

def karg(a: 's', b: (1, 255), c: int = 12) -> int:
    return a + b + c

print(karg("Ham", "spam", "nam"))
print(karg.__annotations__)
    
L = range(0 , 255)
x = list(map(lambda y: y**2, L))
print(x)

xxx = list(filter((lambda x: x > 0), range(-100, 100)))
print(xxx)
    