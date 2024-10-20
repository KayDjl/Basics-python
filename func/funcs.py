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
    