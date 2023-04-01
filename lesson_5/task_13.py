#Задача 26:  Напишите программу, которая на вход принимает 
#два числа A и B, и возводит число А в целую степень B с 
#помощью рекурсии.

import math

A = int(input("введите число: "))
B = int(input("введите степень: "))

def fun(A, B):
    if B == 0:
        return 1
    else:
        return A*fun(A, B-1)
    
    
V = fun(A, B)
print(V)