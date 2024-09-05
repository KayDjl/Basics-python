"""
while True:
    x = input("Enter text: ")
    if x == "stop": break
    print(x)

while True:
    y = input("Enter text: ")
    if y == 'stop':
        break
    elif y.isalpha():
        print(y * 8)
    else:
        num = int(y)
        if num < 20:
            print('low')
        else:
            print(num ** 3)
"""

nu, pu = 1, 2
nudle, wingde = nu, pu
print(nudle, wingde)

string = "SPAM"
(a, b), c = string[:2], string[2:]
print(a,b,c)

L = [1, 2, 3, 4]
while True:
    font, L = L[0], L[1:]
    print(font, L)
        