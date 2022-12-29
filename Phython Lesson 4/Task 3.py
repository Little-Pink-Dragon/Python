lst = list(map(int, input("Введите числа по порядку через пробел:\n").split()))
print(f"Список введенных чисел: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список неповторяющихся элементов: {new_lst}")