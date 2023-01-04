number = input("Введите числа по-порядку: ")
seq = list(number)
print("Последовательность чисел:")
for i, val in enumerate (seq, start = 1):
    
    print(f'№ {i} => {val}')