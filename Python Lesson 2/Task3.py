from random import uniform
Array = int(input('Определите размер массива'))
list1 = []
for i in range(Array):
    f = uniform(0, 9)
    list1.append(round(f, 2))
min = list1[0]
max = 0
for i in range(len(list1)):
    if max < list1[i]:
      max = list1[i]
    if min > list1[i]:
        min = list1[i]
dif = (max - int(max)) - (min - int(min))
print(f"{list1}: Максимальное - {max}, Минимальное - {min}, Разница => {round(dif,2)}")
