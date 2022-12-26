numbers = [4, 9, 16, 25, 36, 49, 64]
summ = 0
for i in range(1, len(numbers), 2):
     if i % 2 == 1:
         summ += numbers[i]       
print(f"{numbers} -> сумма чисел на нечётных позициях равняется: {summ}")