
import sqlite3

def get_contacts(cursor):
    cursor.execute("select * from subscribers")
    results = cursor.fetchall()
    return results

def get_contact(item, cursor):
    cursor.execute(f"select * from subscribers where surname like '%{item}%'"
                    f"or name like '%{item}%'")
    results = cursor.fetchall()
    if results:
        return results
    return "Контакт не найден\n/start - Чтобы вернуться в начальное меню"

def new_contact(data, conn, cursor):
    name, surname, Number = data
    cursor.execute(
    f"insert into subscribers (name, surname, Number) "
    f"values ('{name}', '{surname}', {Number})")
    conn.commit()

def delete(id, conn, cursor):
    try:
        cursor.execute(
            f"delete from subscribers where id={id}")
        conn.commit()
        return 'Контакт был удален \n/start - Чтобы вернуться в начальное меню'
    except:
        return 'Контакт не найден. Попробуйте ещё раз\n/start'