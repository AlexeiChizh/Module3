# Используем встроенную библиотеку math + формула Герона

import math

def area(a,b,c):
    p = (a + b + c) / 2 
    area = math.sqrt(p * (p - a) * (p - b) * (p - c)) 
    area = round(area, 2)
    return area

a = float(input('Length A:   '))
b = float(input('Length B:   '))
c = float(input('Length C:   '))

print('Triangle Area is:',area(a, b, c))