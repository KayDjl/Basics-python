#coding: utf-8
choice = 'pet'
#Аналог switch\case
print({"yert": 1.22,
       "peri": 183,
       "pet": 1.77,
       "uli": 99} [choice])

bec = {'spam': 1,
       'len': 2,
       'ter': 3}
print(bec.get('spam', 'Bad choice'))
print(bec.get('heri', 'Bad choice'))