from view import *
from model import * 
from modelTXT import *    

def main():
    while True:

        select = show_menu()

        if select == 1:
            people = get_people()
            people_txt = get_people_txt()
            show_people(people, people_txt)
        elif select == 2:
            while True:
                text = file_selection()
                if text == 1:
                    man = add_menu()
                    add(man)
                    show_result("Запись добавлена")
                    break
                elif text == 2:
                    man_txt = add_menu_txt()
                    add_txt (man_txt)
                    show_result("Запись добавлена")
                    break
                elif text == 3:
                    man = add_menu()
                    add(man)
                    add_txt(man)
                    show_result("Запись добавлена")
                    break
                else:
                    print("Выберите 1, 2 или 3 вариант")    
        elif select == 3:
             while True:
                text_del = file_selection_del()
                if text_del == 1:
                    number = delet_menu()
                    delet(number)
                    show_result("Запись удалена")
                    break
                elif text_del == 2:
                    number_txt = delet_menu_txt()
                    delet_txt(number_txt)
                    show_result("Запись удалена")
                    break
                elif text_del == 3:
                    number = delet_menu()
                    delet(number)
                    delet_txt(number)
                    show_result("Запись удалена")
                    break
                else:
                    print("Выберите 1, 2 или 3 вариант")
        elif select == 4:
            show_result("Возвращайтесь снова")
            break