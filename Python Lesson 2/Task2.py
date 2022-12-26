from random import randint
Array = int(input('Определите размер массива'))
list = []
list_2 = []
for i in range(Array):
    list.append(randint(0, 9))
for i in range(len(list)):
    while i < len(list)/2 and Array > len(list)/2:
        Array = Array - 1
        a = list[i] * list[Array]
        list_2.append(a)
        i += 1
print(f"{list} => {list_2}")