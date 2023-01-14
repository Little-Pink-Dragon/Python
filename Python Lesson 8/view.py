
def show_menu():
    print("Выберите действие: \n 1 - Показать всех сотрудников"
    " \n 2 - Добавить сотрудника "
    " \n 3 - Удалить сотрудника"
    " \n 4 - Выход")
    select = int(input())
    return select

def file_selection():
    print(f"В какой файл хотите добавить текст?"
    "\n 1. В CSV файл"
    "\n 2. В TXT файл"
    "\n 3. В оба файла")
    text = int(input())
    return text

def file_selection_del():
    print(f"В каком файле хотите удалить запись?"
    "\n 1. В CSV файле"
    "\n 2. В TXT файле"
    "\n 3. В двух файлах")
    text_del = int(input())
    return text_del

def add_menu():
    print(f"Введите ФИО и номер телефона через пробел")
    man = input().split()
    return man

def add_menu_txt():
    print(f"Введите ФИО и номер телефона через пробел")
    man_txt = input().split()
    return man_txt

def delet_menu():
    print(f"Введите номер записи для удаления")
    delet = int(input())-1
    return delet

def delet_menu_txt():
    print(f"Введите номер записи для удаления")
    delet_txt = int(input())-1
    return delet_txt

def show_result(msg):
    print(msg)

def show_people(people, people_txt):
    print("\nСписок в CSV:\n№\tФамилия\tИмя\tНомер телефона")
    for i,p in enumerate(people):
        print(i+1,*p, sep = "\t")
    print("\nСписок в TXT:\n№\tФамилия\tИмя\tНомер телефона")
    for i,p in enumerate(people_txt):
        print(i+1,*p, sep = "\t")