#Задача 20:

#В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
#В случае с английским алфавитом очки распределяются так:
#A, E, I, O, U, L, N, S, T, R – 1 очко;
#D, G – 2 очка;
#B, C, M, P – 3 очка;
#F, H, V, W, Y – 4 очка;
#K – 5 очков;
#J, X – 8 очков;
#Q, Z – 10 очков.

#А русские буквы оцениваются так:
#А, В, Е, И, Н, О, Р, С, Т – 1 очко;
#Д, К, Л, М, П, У – 2 очка;
#Б, Г, Ё, Ь, Я – 3 очка;
#Й, Ы – 4 очка;
#Ж, З, Х, Ц, Ч – 5 очков;
#Ш, Э, Ю – 8 очков;
#Ф, Щ, Ъ – 10 очков.
#Напишите программу, которая вычисляет стоимость введенного пользователем слова.
#Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#Ввод: ноутбук
#Вывод: 12
import random

list_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R',
          'D', 'G','B', 'C', 'M', 'P','F', 'H', 'V', 'W', 'Y','K', 'J', 'X' , 'Q', 'Z']
list_number = [1, 2, 3, 4, 5, 8, 10]
list_2 = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т','Д', 
          'К', 'Л', 'М', 'П', 'У','Б', 'Г', 'Ё', 'Ь', 'Я','Й', 'Ы','Ж', 'З', 'Х', 'Ц', 'Ч','Ш', 'Э', 'Ю','Ф', 'Щ', 'Ъ']

dict_english = {**{el: list_number[0] for el in list_1[:10]},**{el: list_number[1] for el in list_1[10:12]}, 
                **{el: list_number[2] for el in list_1[12:16]}, **{el: list_number[3] for el in list_1[16:20]},
                **{el: list_number[4] for el in list_1[21]},**{el: list_number[5] for el in list_1[22:24]},
                **{el: list_number[6] for el in list_1[24:26]}}
dict_rus = {**{el: list_number[0] for el in list_2[:9]},**{el: list_number[1] for el in list_2[9:15]}, 
                **{el: list_number[2] for el in list_2[15:20]}, **{el: list_number[3] for el in list_2[20:22]},
                **{el: list_number[4] for el in list_2[22:27]},**{el: list_number[5] for el in list_2[27:30]},
                **{el: list_number[6] for el in list_2[30:33]}}
str_1 = input("введите строку ")
count = 0
merge_dict = dict_english | dict_rus
for el in str_1.upper():
    if el in merge_dict:
        count += merge_dict[el]
print(count)
  
print(dict_english)
print(dict_rus)


