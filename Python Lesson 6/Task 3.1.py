numbers = [4, 9, 16, 25, 36, 49, 64]
def filter_even_num(in_num):
    if(in_num % 2) == 1:
        return True
    else:
        return False
out_filter = filter(filter_even_num, numbers)
print("Весь список: ", numbers)
print("Список нечетных чисел: ", list(out_filter))