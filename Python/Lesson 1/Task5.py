Ax = float(input('Введите координаты точки A по оси x: '))
Ay = float(input('Введите координаты точки A по оси y: '))
Bx = float(input('Введите координаты точки B по оси x: '))
By = float(input('Введите координаты точки B по оси y: '))
distance = (((Ax-Bx)**2+(Ay-By)**2)**0.5)
print(f'Расстояние между точкой A и точкой B = {distance}' )
