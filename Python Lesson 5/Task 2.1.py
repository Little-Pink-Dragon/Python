import random
player1 = input("Имя своё имя: ")
player2 = str("Sam")
print("С вами играет Искусственный Интелект: ", player2)
game = random.randrange(1,3)
candies = int(random.randrange(28,200))
print("Необходимо по очереди брать конфеты. Максимальное колличество конфет, которое вы можете взять: 28. Всего конфет: ", candies)
if game == 1:
    print("Ход делает: ", player1)
    while candies > 0:
        if candies > 28:
            print(f'{player1} берет колличество конфет: ')
            motion1 = int(input())
            if motion1 > 28:
                print ("Вы взяли больше 28 конфет. Максимально допустимое число 28!")
                candies = candies - 28
            else:
                candies = candies - motion1
        if candies <= 28:
            print(f'Осталось {candies} конфет(ы), их забирает {player2}. Поздравляю, {player2} - победитель!!!')
            break
        if candies > 28:
            motion2 = random.randrange(1,29)
            print(f'{player2} берет колличество конфет: ', motion2)
            candies = candies - motion2
        if candies <= 28:
            print(f'Осталось {candies} конфет(ы), их забирает {player1}. Поздравляю, {player1} - победитель!!!')
            break
else:
    print("Ход делает: ", player2)
    while candies > 0:
        if candies > 28:
            motion2 = random.randrange(1,29)
            print(f'{player2} берет колличество конфет: ', motion2)
            candies = candies - motion2
        if candies <= 28:
            print(f'Осталось {candies} конфет(ы), их забирает {player1}. Поздравляю, {player1} - победитель!!!')
            break
        if candies > 28:
            print(f'{player1} берет колличество конфет: ')
            motion1 = int(input())
            if motion1 > 28:
                print ("Вы взяли больше 28 конфет. Максимально допустимое число 28!")
                candies = candies - 28
            else:
                candies = candies - motion1
        if candies <= 28:
            print(f'Осталось {candies} конфет(ы), их забирает {player2}. Поздравляю, {player2} - победитель!!!')
            break