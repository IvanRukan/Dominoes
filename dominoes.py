import random
placeholder = 0
y = 0
str_snake = ''
str_comp = ''
value0 = 0
value1 = 0
value2 = 0
value3 = 0
value4 = 0
value5 = 0
value6 = 0
score = dict()
order = []
player = []
computer = []
stock = []
status = ''
pairs = []
snake = ''
inp_emp = ' '
player_input = ' '
allowed = ['1','2','3','4','5','6','7', '8', '9', '10', '11', '12']
allowed_n = ['-1','-2','-3','-4','-5','-6','-7', '-8', '-9', '-10', '-11', '-12']
illegal = 0
illegal1 = 0
dominoes = [[x, y] for x in range(0, 7) for y in range(x, 7)]
while status == '':
    dominoes = [[x, y] for x in range(0, 7) for y in range(x, 7)]
    random.shuffle(dominoes)
    while len(player) != 7:
        a = random.choice(dominoes)
        player.append(a)
        dominoes.remove(a)
    while len(computer) != 7:
        a = random.choice(dominoes)
        computer.append(a)
        dominoes.remove(a)
    stock = dominoes
    if [6, 6] in player:
        snake = [6, 6]
        player.remove([6, 6])
        status = 'computer'
        break

    elif [6, 6] in computer:
        snake = [6, 6]
        computer.remove([6, 6])
        status = 'player'
        break
    if [5, 5] in player:
        snake = [5, 5]
        player.remove([5, 5])
        status = 'computer'
        break

    elif [5, 5] in computer:
        snake = [5, 5]
        computer.remove([5, 5])
        status = 'player'
        break
    if [4, 4] in player:
        snake = [4, 4]
        player.remove([4, 4])
        status = 'computer'
        break

    elif [4, 4] in computer:
        snake = [4, 4]
        computer.remove([4, 4])
        status = 'player'
        break
    if [3, 3] in player:
        snake = [3, 3]
        player.remove([3, 3])
        status = 'computer'
        break

    elif [3, 3] in computer:
        snake = [3, 3]
        computer.remove([3, 3])
        status = 'player'
        break
    if [2, 2] in player:
        snake = [2, 2]
        player.remove([2, 2])
        status = 'computer'
        break

    elif [2, 2] in computer:
        snake = [2, 2]
        computer.remove([2, 2])
        status = 'player'
        break
    if [1, 1] in player:
        snake = [1, 1]
        player.remove([1, 1])
        status = 'computer'
        break

    elif [1, 1] in computer:
        snake = [1, 1]
        computer.remove([1, 1])
        status = 'player'
        break
    if [0, 0] in player:
        snake = [0, 0]
        player.remove([0, 0])
        status = 'computer'
        break

    elif [0, 0] in computer:
        snake = [0, 0]
        computer.remove([0, 0])
        status = 'player'
        break
snake = [snake]
while status != 'Status: The game is over. You won!' or status != 'Status: The game is over. The computer won!' or status != "Status: The game is over. It's a draw!":
    print('=' * 70)
    print('Stock size: ' + str(len(stock)))
    print('Computer pieces: ' + str(len(computer)))
    print()
    snake1 = str(snake)
    if len(snake) > 6:
        print(str(snake[0]) + str(snake[1]) + str(snake[2]) + '...' + str(snake[-3]) + str(snake[-2]) + str(snake[-1]))
        snake1 = snake1.lstrip('[')
        snake1 = snake1.rstrip(']')
    else:
        snake1 = snake1.lstrip('[')
        snake1 = snake1.rstrip(']')
        print('[' + snake1 + ']')
    print()
    print('Your pieces:')
    for i in range(len(player)):
        print(str(i + 1) + ':' + str(player[i]))
    print()
    if status == 'computer':
        if len(player) == 0:
            status = 'Status: The game is over. You won!'
            print(status)
            break
        print('Status: Computer is about to make a move. Press Enter to continue...')
        while inp_emp != '':
            inp_emp = input()
            if inp_emp != '':
                print('Invalid input. Please try again.')
                continue
            if len(computer) != 0:
                str_comp = str(computer)
                value0 = str_comp.count('0')
                value1 = str_comp.count('1')
                value2 = str_comp.count('2')
                value3 = str_comp.count('3')
                value4 = str_comp.count('4')
                value5 = str_comp.count('5')
                value6 = str_comp.count('6')
                str_snake = str(snake)
                value0 = value0 + str_snake.count('0')
                value1 = value1 + str_snake.count('1')
                value2 = value2 + str_snake.count('2')
                value3 = value3 + str_snake.count('3')
                value4 = value4 + str_snake.count('4')
                value5 = value5 + str_snake.count('5')
                value6 = value6 + str_snake.count('6')
                for i in computer:
                    x = str(i)
                    if '0' in x:
                        y = y + value0
                    if '1' in x:
                        y = y + value1
                    if '2' in x:
                        y = y + value2
                    if '3' in x:
                        y = y + value3
                    if '4' in x:
                        y = y + value4
                    if '5' in x:
                        y = y + value0
                    if '6' in x:
                        y = y + value6
                    score[y] = i
                    order.append(y) #ПРИСВАИВАЕМ ЗНАЧЕНИЕ ПО ОДНОМУ КЛЮЧУ
                    y = 0
                order.sort()
                counter = len(snake)
                while counter == len(snake):
                    if len(order) == 0:
                        if len(stock) != 0:
                            computer.append(stock.pop())
                            break
                        else:
                            placeholder += 1
                            break
                    control = score[order[-1]]
                    if control[0] == snake[-1][-1]:
                        snake.append(control)
                        computer.remove(control)
                    elif control[1] == snake[-1][-1]:
                        computer.remove(control)
                        control = control[::-1]
                        snake.append(control)
                    elif control[1] == snake[0][0]:
                        snake.insert(0,control)
                        computer.remove(control)
                    elif control[0] == snake[0][0]:
                        snake.insert(0, control[::-1])
                        computer.remove(control)
                    else:
                        order.pop()
        inp_emp = ' '
        status = 'player'
        score = dict()
        order = []
    elif status == 'player':
        if len(computer) == 0 or illegal == 1:
            status = 'Status: The game is over. The computer won!'
            print(status)
            break
        print("Status: It's your turn to make a move. Enter your command.")
        while player_input not in allowed and player_input not in allowed_n and player_input != '0':
            player_input = input()
            if player_input not in allowed and player_input not in allowed_n and player_input != '0':
                print('Invalid input. Please try again.')
                continue
            elif int(player_input) > len(player):
                print('Invalid input. Please try again.')
                continue
            if player_input in allowed:
                turn = int(player_input)
                mark = player[turn - 1]
                mark = str(mark)
                if mark[1] == snake1[-1] or mark[-2] == snake1[-1]:
                    if mark[1] == snake1[-1]:
                        snake.append(player[turn - 1])
                        del player[turn - 1]
                    else:
                        x = player[turn - 1]
                        snake.append(x[::-1])
                        del player[turn - 1]
                else:
                    print('Illegal move. Please try again.')
                    player_input = ' '
                    continue
            elif player_input in allowed_n:
                turn = int(player_input)
                turn = abs(turn)
                mark = player[turn - 1]
                mark = str(mark)
                if mark[1] == snake1[0] or mark[-2] == snake1[0]:
                    if mark[-2] == snake1[0]:
                        snake.insert(0, player[turn - 1])
                        del player[turn - 1]
                    else:
                        x = player[turn - 1]
                        snake.insert(0, x[::-1])
                        del player[turn - 1]
                else:
                    print('Illegal move. Please try again.')
                    player_input = ' '
                    continue
            elif player_input == '0':
                if len(stock) != 0:
                    player.append(stock.pop())
                else:
                    placeholder += 1
                    break
        player_input = ' '
        status = 'computer'
    if snake1[1] == snake1[-2] and snake1.count(snake1[1]) == 8 or placeholder > 1:
        status = "Status: The game is over. It's a draw!"
        print(status)









