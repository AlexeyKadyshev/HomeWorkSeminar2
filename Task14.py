#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
#не превосходящие числа N.

from math import pow
degree = 1
result = 2
num = int(input("Введите верхний предел: "))
while  result <= num:
    print(int(result))
    degree += 1
    result = pow(2, degree)
    
