str = input("Введите РО в одну строку:  ").split(sep='О')
str=[len(n) for n in str]
str.sort()
print(f'Максимально колличество решек подряд: {str[-1]} раз(а)')