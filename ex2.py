'''Требуется найти в массиве A[1..N] 
самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит 
натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
'''

n = int(input('Введите количество элементов в массиве:'))
from random import randint
a = [randint(1,n) for i in range(0,n)]
a[0],a[n-1]=1,n
print(a)
x = int(input('Введите искомое число:'))
y = a[0]
z = a[0]
for i in range(1,len(a)):
    if abs(x-y) > abs(x-a[i]):
        y=a[i]
    elif x-y == -(x-a[i]):
        z=a[i]
if x-y == -(x-z):
    print(f"Самые близкие элементы в массиве к числу {x}: {y}, {z}") 
else:
    print(f"Самый близкий элемент в массиве к числу {x}: {y}") 