number = int(input('Введите день недели: '))

if number < 1 or number > 7:
    print('В неделе 7 дней! Введите число от 1 до 7')
elif number > 5:
    print('Это выходной')
else:
    print('Это рабочий день')