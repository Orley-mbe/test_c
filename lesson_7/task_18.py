#Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
#которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
#Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
#Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения. 

import math
import random

def fun(x, y):
    matrix = [random.randint(0,100) for i in range(x) for j in range(y)]
    #print(matrix)
    return matrix.pop(x*y - 1)

def print_operation_table(operation, num_rows=6, num_columns=6):
    return operation(num_rows, num_columns)

 
print(print_operation_table(fun, 5, 6))
        






