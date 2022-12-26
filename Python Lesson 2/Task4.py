Binary_number = ""
number = int(input("Введите число, чтобы преобразовать его в двоичное число:\n"))
n = number
while number != 0:
    Binary_number = str(number % 2) + Binary_number
    number //= 2
print(f"{n} -> {Binary_number}")