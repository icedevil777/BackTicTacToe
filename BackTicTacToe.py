"""
Гуляев Григорий Атанольевич
Крестики-Нолики.
"""
import copy
import random
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)
"""Формирование элементов игрового поля"""
PLAY_BOARD = [str(num) for num in range(0, 100)]
for i in range(9):
    PLAY_BOARD[i] = " " + PLAY_BOARD[i + 1] + " "
for i in range(9, 99):
    PLAY_BOARD[i] = PLAY_BOARD[i + 1] + " "
PLAY_BOARD[99] = "100"



PLAYERS_MARKS = ['X', 'O']

def Sectors(PLAY_BOARD):
    """Функция разбивает всё поле на отдельные сектора"""
    HorizontSectors = []
    i = 0
    n = 0
    k = 0
    while i < 10:
        HorizontSectors.append(PLAY_BOARD[i+n:10+k])
        i = i + 1
        n = n + 9
        k = k + 10

    VerticalSectors = []
    i = 0
    while i < 10:
        VerticalSectors.append(PLAY_BOARD[i:100:10])
        i = i + 1

    DiagonalSectorsLtoR = [] # Слева направо
    i = 0
    n = 10  # Данная переменная определяет разность длин соседних диагональ с правой стороны квадрата!
    while i < 6:
        DiagonalSectorsLtoR.append(PLAY_BOARD[i:10*n:11])
        i = i + 1
        n = n - 1
    i = 10
    n = 1 # Данная переменная определяет разность длин соседних диагональ с верхней стороны квадрата!
    while i < 51:
        DiagonalSectorsLtoR.append(PLAY_BOARD[i:100-n:11])
        i = i + 10
        n += 1

    DiagonalSectorsRtoL = [] # Справа налево
    i = 4
    n = 10  # Данная переменная определяет разность длин соседних диагональ с левой стороны квадрата!
    while i < 10:
        DiagonalSectorsRtoL.append(PLAY_BOARD[i:31+n:9])
        i = i + 1
        n = n + 10
    i = 29
    n = 1 # Данная переменная определяет разность длин соседних диагональ с верхней стороны квадрата!
    while i < 60:
        DiagonalSectorsRtoL.append(PLAY_BOARD[i:92+n:9])
        i = i + 10
        n += 1

    """Ввиду того обстоятельства, что диагональные сектора представляют собой рваные списки, необходимо дополнить их нулями:"""
    for i in range(10):
        SectorLength = len(DiagonalSectorsRtoL[i])
        if SectorLength < 10:
            for j in range(10 - SectorLength):
                DiagonalSectorsRtoL[i].append("0")

    for i in range(10):
        SectorLength = len(DiagonalSectorsLtoR[i])
        if SectorLength < 10:
            for j in range(10 - SectorLength):
                DiagonalSectorsLtoR[i].append("0")

    SECTORS = [HorizontSectors, VerticalSectors, DiagonalSectorsRtoL, DiagonalSectorsLtoR]
    return SECTORS

def display_board(board_list):
    """Вывод элементов игрового поля в командную строку"""
    print(" " + " -----------------------------------------------------------" + "")
    print(' ¦ ' + board_list[90] + ' ¦ ' + board_list[91] + ' ¦ ' + board_list[92] + ' ¦ ' + board_list[93] + ' ¦ ' + board_list[94] + ' ¦ ' + board_list[95] + ' ¦ ' + board_list[96] + ' ¦ ' + board_list[97] + ' ¦ ' + board_list[98] + ' ¦ ' + board_list[99] + ' ¦ ')
    print(' ¦' + "-----------------------------------------------------------" +'¦')
    print(' ¦ ' + board_list[80] + ' ¦ ' + board_list[81] + ' ¦ ' + board_list[82] + ' ¦ ' + board_list[83] + ' ¦ ' + board_list[84] + ' ¦ ' + board_list[85] + ' ¦ ' + board_list[86] + ' ¦ ' + board_list[87] + ' ¦ ' + board_list[88] + ' ¦ ' + board_list[89] + ' ¦ ')
    print(' ¦' + "-----------------------------------------------------------" +'¦')
    print(' ¦ ' + board_list[70] + ' ¦ ' + board_list[71] + ' ¦ ' + board_list[72] + ' ¦ ' + board_list[73] + ' ¦ ' + board_list[74] + ' ¦ ' + board_list[75] + ' ¦ ' + board_list[76] + ' ¦ ' + board_list[77] + ' ¦ ' + board_list[78] + ' ¦ ' + board_list[79] + ' ¦ ')
    print(' ¦' + "-----------------------------------------------------------" +'¦')
    print(' ¦ ' + board_list[60] + ' ¦ ' + board_list[61] + ' ¦ ' + board_list[62] + ' ¦ ' + board_list[63] + ' ¦ ' + board_list[64] + ' ¦ ' + board_list[65] + ' ¦ ' + board_list[66] + ' ¦ ' + board_list[67] + ' ¦ ' + board_list[68] + ' ¦ ' + board_list[69] + ' ¦ ')
    print(' ¦' + "-----------------------------------------------------------" +'¦')
    print(' ¦ ' + board_list[50] + ' ¦ ' + board_list[51] + ' ¦ ' + board_list[52] + ' ¦ ' + board_list[53] + ' ¦ ' + board_list[54] + ' ¦ ' + board_list[55] + ' ¦ ' + board_list[56] + ' ¦ ' + board_list[57] + ' ¦ ' + board_list[58] + ' ¦ ' + board_list[59] + ' ¦ ')
    print(' ¦' + "-----------------------------------------------------------" +'¦')
    print(' ¦ ' + board_list[40] + ' ¦ ' + board_list[41] + ' ¦ ' + board_list[42] + ' ¦ ' + board_list[43] + ' ¦ ' + board_list[44] + ' ¦ ' + board_list[45] + ' ¦ ' + board_list[46] + ' ¦ ' + board_list[47] + ' ¦ ' + board_list[48] + ' ¦ ' + board_list[49] + ' ¦ ')
    print(' ¦' + "-----------------------------------------------------------" +'¦')
    print(' ¦ ' + board_list[30] + ' ¦ ' + board_list[31] + ' ¦ ' + board_list[32] + ' ¦ ' + board_list[33] + ' ¦ ' + board_list[34] + ' ¦ ' + board_list[35] + ' ¦ ' + board_list[36] + ' ¦ ' + board_list[37] + ' ¦ ' + board_list[38] + ' ¦ ' + board_list[39] + ' ¦ ')
    print(' ¦' + "-----------------------------------------------------------" +'¦')
    print(' ¦ ' + board_list[20] + ' ¦ ' + board_list[21] + ' ¦ ' + board_list[22] + ' ¦ ' + board_list[23] + ' ¦ ' + board_list[24] + ' ¦ ' + board_list[25] + ' ¦ ' + board_list[26] + ' ¦ ' + board_list[27] + ' ¦ ' + board_list[28] + ' ¦ ' + board_list[29] + ' ¦ ')
    print(' ¦' + "-----------------------------------------------------------" +'¦')
    print(' ¦ ' + board_list[10] + ' ¦ ' + board_list[11] + ' ¦ ' + board_list[12] + ' ¦ ' + board_list[13] + ' ¦ ' + board_list[14] + ' ¦ ' + board_list[15] + ' ¦ ' + board_list[16] + ' ¦ ' + board_list[17] + ' ¦ ' + board_list[18] + ' ¦ ' + board_list[19] + ' ¦ ')
    print(' ¦' + "-----------------------------------------------------------" +'¦')
    print(' ¦ ' + board_list[0]  + ' ¦ ' + board_list[1]  + ' ¦ ' + board_list[2]  + ' ¦ ' + board_list[3]  + ' ¦ ' + board_list[4]  + ' ¦ ' + board_list[5]  + ' ¦ ' + board_list[6]  + ' ¦ ' + board_list[7]  + ' ¦ ' + board_list[8]  + ' ¦ ' + board_list[9]  + ' ¦ ')
    print(" " + " -----------------------------------------------------------" + "")

def size_choice():
    """Выберите сторону!"""
    player = ''
    while player not in ('X', 'O'):
        player = input('             Выберите сторону: X или O: ').upper()

    if player == 'X':
        art_int = 'O'
    else:
        art_int = 'X'
    print(f'     Вы выбрали "{player}" Отличный выбор! Удачной игры!')

    Player_Mark = " " + str(player) + " "
    AI_Mark = " " + str(art_int) + " "

    return Player_Mark, AI_Mark

def Rand_Fill(PLAY_BOARD):
    """Игроку предлагается добавить на поле некоторое количество O и X """
    while True:
        try:
            Markers = int(input(" Введите число от 0 до 50 % для заполнения поля игры!"))
            if Markers < 91:
                step = set()
                for i in range(Markers):
                    step.add(random.randint(0, 99))
                list_step = list(step)
                for i in range(len(list_step)):
                    if (i % 2) == 0:
                        PLAY_BOARD[list_step[i]] = " X "
                    else:
                        PLAY_BOARD[list_step[i]] = " O "
            else:
                print(Fore.RED + " Введите корректное число! ")
                continue
            break
        except ValueError:
            print(Fore.RED + " Неверное значение!")

def PlayerStep(PLAY_BOARD, s_h):
    i = 1
    while True:
        try:
            PlayerIn = input(" Ваш ход! Введите значение поля от 1 до 60! ")
            if int(PlayerIn) < 95:
                if PLAY_BOARD[int(PlayerIn) - 1] == s_h[0] or PLAY_BOARD[int(PlayerIn) - 1] == s_h[1] or int(PlayerIn) < 1:
                    print(Fore.RED + " Неверный ход!")
                    continue
                else:
                    PLAY_BOARD[int(PlayerIn) - 1] = s_h[0]
                    break
            else:
                print(Fore.RED + " Неверный ход!")
                continue
        except ValueError:
            print(Fore.RED + " Неверное значение!")

def AIStep(PLAY_BOARD, s_h):
    chance = 0  # Компьютер имеет несколько попыток переходить в случае провала!
    while True:
        ai_step = random.randint(1, 99)
        #ai_step = int(input("Введите цифру ")) - 1
        if PLAY_BOARD[ai_step] == s_h[0] or PLAY_BOARD[ai_step] == s_h[1]:
            continue
        else:
            PLAY_BOARD_Draft = copy.copy(PLAY_BOARD)  # PLAY_BOARD_Draft использует AI для своих личных манипуляций!
            PLAY_BOARD_Draft[ai_step] = s_h[1]
            if AiAnalysis(Sectors(PLAY_BOARD_Draft), s_h) == 1:
                PLAY_BOARD[ai_step] = s_h[1]
                break
            else:
                chance = chance + 1
                if chance < 1000:  # Таким образом можно слегка менять уровень сложности бота!
                    continue
                else:
                    PLAY_BOARD[ai_step] = s_h[1]
                    break

    return ai_step

def Analysis(SECTORS,Markets):
    """Функция определяет победителя и завершает игру!"""
    play = 1
    for a in range(4):
        for b in range(10):
            for c in range(6):
                if SECTORS[a][b][c] == s_h[0] and SECTORS[a][b][c + 1] == s_h[0] and SECTORS[a][b][c + 2] == s_h[0] and SECTORS[a][b][c + 3] == s_h[0] and SECTORS[a][b][c + 4] == s_h[0]:
                    play = 0
                    print(Fore.RED + " Игра окончена. ВЫ ПРОИГРАЛИ!")
                    break
                if SECTORS[a][b][c] == " O " and SECTORS[a][b][c + 1] == s_h[1] and SECTORS[a][b][c + 2] == s_h[1] and SECTORS[a][b][c + 3] == s_h[1] and SECTORS[a][b][c + 4] == s_h[1]:
                    play = 0
                    print(Fore.GREEN + " Игра окончена. КОМПУКТЕР ПОРАЖЕН!")
                    break
    return play

def AiAnalysis(SECTORS,Markets):
    """Функция определяет поведение Ai !"""
    test = 1
    for a in range(4):
        for b in range(10):
            for c in range(6):
                if SECTORS[a][b][c] == " O " and SECTORS[a][b][c + 1] == s_h[1] and SECTORS[a][b][c + 2] == s_h[1] and SECTORS[a][b][c + 3] == s_h[1] and SECTORS[a][b][c + 4] == s_h[1]:
                    test = 0
                    break
    return test




print(" Добро пожаловать в Крестики-Нолики. Мод - Поддавки! \n       Не забудьте растянуть командную строку!")
s_h = size_choice()
Rand_Fill(PLAY_BOARD)
play = 1
display_board(PLAY_BOARD)
while play:
    PlayerStep(PLAY_BOARD, s_h)
    ai_step = AIStep(PLAY_BOARD, s_h)
    display_board(PLAY_BOARD)

    print(f' Компьютер сходил "{ai_step + 1}" ')

    play = Analysis(Sectors(PLAY_BOARD), s_h)












