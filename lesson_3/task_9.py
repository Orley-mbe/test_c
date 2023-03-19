#Задача 18:
#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
#Заполните массив случайными натуральными числами от 1 до N.
#Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.
#Ввод: 10
#Ввод: 7
#1 2 1 8 9 6 5 4 3 4
#Вывод: 6
import random
N = int(input("введите длину списка "))
X = int(input("введите число "))
list_number = [random.randint(0, N) for el in range(N)]
print(list_number)
result = 0
temp = X
list_result = []
for el in list_number:
    temp_1 = el - X
    print(temp_1)
    if el == X:
        list_number.remove(el)
    elif abs(temp_1) < temp:
        temp = abs(temp_1)
        list_result.append(el)

print(f'Ближайшее число к {X} - {list_result.pop()}')