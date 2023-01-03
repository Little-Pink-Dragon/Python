scheme = list(range(1,10))
print("Добро пожаловать в игру: 'Крестики - нолики'")
player1 = input("Введите имя первого игрока (играет X): ")
player2 = input("Введите имя второго игрока (играет 0): ")
print("Перед Вами поле 3 на 3. Введите число от 1 до 9, чтобы заполнить ячейку")
def drawing(scheme):
    print ("-" * 13)
    for i in range(3):
        print ("|", scheme[0+i*3], "|", scheme[1+i*3], "|", scheme[2+i*3], "|")
        print ("-" * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input(f"Куда поставим {player_token}?: ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(scheme[player_answer-1]) not in "XO"):
                scheme[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта ячейка уже занята, выберите другую клетку!")
        else:
            print ("Такой ячейки нет. Введите цифру от 1 до 9")

def check_win(scheme):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if scheme[each[0]] == scheme[each[1]] == scheme[each[2]]:
            return scheme[each[0]]
    return False

def main(scheme):
    counter = 0
    win = False
    while not win:
        drawing(scheme)
        if counter % 2 == 0:
            take_input("X")
            name = player1
        else:
            take_input("O")
            name = player2
        counter += 1
        if counter > 4:
            tmp = check_win(scheme)
            if tmp:
                print (f"Поздравляю, {name} выиграл(а)")
                win = True
                break
        if counter == 9:
            print ("Победила дружба!")
            break
    drawing(scheme)

main(scheme)