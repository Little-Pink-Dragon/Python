square_number = int(input('Введите номер четверти: '))

if square_number == 1:
    print('x > 0; y > 0')
elif square_number == 2:
    print('x < 0; y > 0')
elif square_number == 3:
    print('x < 0; y < 0')
elif square_number == 4:
    print('x > 0; y < 0')
else:
    print('На оси координат только 4 квадрата')
