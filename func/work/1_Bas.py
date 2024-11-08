def seq(x):
    return x

print(seq("Hello"))

def adder(*x):
    x = list(x)
    try:
        return "".join(x) if type(x[0]) == str else sum(x)
    except:
        y = "Неверное значение"
        return y

print(adder("h", "e", "l", "l", "o"))

print(adder(1, 2, 3))
print(type(adder(1, 2, 4, 5, 2, 1)))