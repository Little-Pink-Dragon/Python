text = input("Введите слова через пробел:\n")
print(f"Ваш текст: {text}")
find_text = "абв"
lst = [i for i in text.split() if find_text not in i]
print(f'Результат: {" ".join(lst)}')