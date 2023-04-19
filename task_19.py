#Задача 38:  Дополнить телефонный справочник возможностью изменения и удаления данных. 
#Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
#для изменения и удаления данных.

def read_file(filename):
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            item = line.replace('\n', '').split(sep = ',')
            data_array.append(item)
    return data_array

def write_file(filename, data_array):
    with open(filename, 'w') as data:
       for i in data_array:
           write_item = ", ".join(i)
           data.write(f'{write_item}\n') 
           

def add_item(filename, lastname = '', firstname = '', secondname = '', phone = ''):
    # прочли весь справочник
    #нашли id
    data_array = read_file(filename)
    max_id = 0
    for i in range(1, len(data_array)):
        if max_id < int(data_array[i][0]):
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    print(next_id)
    lastname = input('Фамиоия: ')
    firstname = input('Имя: ')
    secondname = input('Отчество: ')
    phone = input('телефон: ')
    new_item = []
    new_item.append(str(next_id))
    new_item.append(lastname)
    new_item.append(firstname)
    new_item.append(secondname)
    new_item.append(phone)
    print(new_item)
    print(data_array)
    data_array.append(new_item)
    print(data_array)
    write_file(filename, data_array)
    #print('запись добавлена')


def show_all_items(filename):
    data_array = read_file(filename)
    for i in range(1, len(data_array)):
        print("Id: ", data_array[i][0], "Фамилия: ", data_array[i][1], "Имя: ", data_array[i][2], "Отчество: ", data_array[i][3], "телефон: ", data_array[i][4])


def change_items(filename):
    data_array = read_file(filename)
    print(data_array)
    item = int(input('Введите id: '))
    for i in range(1, len(data_array)):
       
        if int(data_array[i][0]) == item:
            data_array[i][1] = input('Фамиоия: ')
            data_array[i][2] = input('Имя: ')
            data_array[i][3] = input('Отчество: ')
            data_array[i][4] = input('телефон: ')
    print(data_array)
    write_file(filename, data_array)
        
            
def delete_item(filename):
    
    data_array = read_file(filename)
    item = int(input('Введите id: '))
    for i in range(1, len(data_array)+1):
        if int(data_array[i][0]) == item:
            data_array.pop(i)
            break
    print(data_array)
    write_file(filename, data_array)


def menu():
    print("Добро пожаловать в справочник")
    print("показать все записи - 1")
    print("Добавить запись - 2")
    print("Изменить запись - 3")
    print("удалить запись - 4")
    user_operation = int(input())

    if user_operation == 1:
        show_all_items(filename)
    elif  user_operation == 2:
        add_item(filename)
    elif  user_operation == 3:
        change_items(filename)
    elif  user_operation == 4:
        delete_item(filename)


filename = 'file.txt'
menu()
#print(read_file(filename))

