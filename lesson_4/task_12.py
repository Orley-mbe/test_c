#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на 
#круглой грядке, причем кусты высажены только по окружности. Таким образом, у 
#каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
#Эти  кусты  обладают  разной  урожайностью,  поэтому  ко  времени  сбора  на  них 
#выросло различное число ягод – на i-ом кусте выросло ai ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
#Эта  система  состоит  из  управляющего  модуля  и  нескольких  собирающих  модулей. 
#Собирающий  модуль  за  один  заход,  находясь  непосредственно  перед  некоторым 
#кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может 
#собрать  за  один  заход  собирающий  модуль,  находясь  перед  некоторым  кустом 
#заданной во входном файле грядки.


import random

N = int(input('Введите кол-во кустов '))
numbers = range(N+1) 
list_dict = {el:random.randint(0, 100) for el in numbers if el != 0} # урожайность кустов
count = 0
m = int(input("введите число входа"))
new_dict = {}
temp = list(list_dict.values())
print(list_dict)
#for el in temp:
 #   if i <= len(temp):


for k in list_dict:
    for el in temp:
        s = list_dict.get(k)
        i = temp.index(s)
        if el == s and 0 < i < len(temp) - 1: 
            count = s + temp[temp.index(s)-1] + temp[temp.index(s)+1]
        elif el == s and i == 0:
            count = s + temp[len(temp)-1] + temp[temp.index(s)+1]
        elif el == s and i == len(temp) - 1 :
            count = s + temp[0] + temp[temp.index(s)-1]
        new_dict.update({list_dict[k]: count})
print(new_dict)
print(max(new_dict.values()))
