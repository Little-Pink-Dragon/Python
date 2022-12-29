N = int(input("Введите натурально число: "))
i = 2 
lst = []
num = N
while i <= N:
    if N % i == 0:
        lst.append(i)
        N //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {num}: {lst}")