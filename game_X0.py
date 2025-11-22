import random

GAMERS = ['X ', '0 ']

def menu():
    print(f"+----------------------------------------------+")
    print(f"|           Игра: 'Крестики Нолики'            |")
    print(f"+----------------------------------------------+")
    print(f"|Автор: Zhabbarov_R_M                          |")
    print(f"+----------------------------------------------+")
    print(f"Меню игры:")
    print(f"1. Начало игры")
    print(f"0. Выход из игры")

def begin():
    # Отрисовка поля
    pole = [['- ', '- ', '- '],
            ['- ', '- ', '- '],
            ['- ', '- ', '- ']]
    return pole

def look_pole(pole):
    # Просмотр поля
    tire = ['===|'] * 3
    print(f'~~|| 0 | 1 | 2 |')
    print(f'--||{"".join(tire)}')
    print(f'0 || {"| ".join(pole[0])}|')
    print(f'1 || {"| ".join(pole[1])}|')
    print(f'2 || {"| ".join(pole[2])}|')

def step(pole, who):
    # Ходы в игре
    trig = True
    while trig:
        try:
            x, y = int(input('Строка: ')), int(input('Графа: '))
            if (x in range(0,3)) & (y in range(0,3)):
                if pole[x][y] == '- ':
                    pole[x][y] = who
                    trig = False
                else:
                    print(f'Данные в ячейке уже введены')
                    print(f'{who[0]}-ик, попробуй еще раз и будь внимателен')
            else:
                print(f'Выходи за рамки, но не в этой игре (некорректные координаты)')
                print(f'{who[0]}-ик, попробуй еще раз и будь внимателен')
        except:
            print(f'Нужно вводить только цифры')
    return pole

def win(pole):
    for who in GAMERS:
        msg = f'Выграл {who[0]}-ик! Молодец!!! \n Конец игры \n ----------------------'
        for i in range(0, 3):
            if pole[i] == [_ for _ in pole[i] if _ == who]:
                print(f'{msg}')  # По строкам
                return True
            list_cells = [pole[0][i]] + [pole[1][i]] + [pole[2][i]]
            if list_cells == [_ for _ in list_cells if _ == who]:
                print(f'{msg}')  # По столбцам
                return True
        list_cells = [pole[i][i] for i in range(0, 3)]
        if list_cells == [_ for _ in list_cells if _ == who]:
            print(f'{msg}')  # По убывающей диагонали
            return True
        list_cells = [pole[2][0]] + [pole[1][1]] + [pole[0][2]]
        if list_cells == [_ for _ in list_cells if _ == who]:
            print(f'{msg}')  # По возрастающей диагонали
            return True
    return False

def check(pole):
    # Проверка на ничью
    msg = f'Ничья'
    list_cells = []
    for i in range(0, 3):
        list_cells += [_ for _ in pole[i] if _ == '- ']
    if len(list_cells)==0:
        print(f'{msg}')  # По строкам
        return True
    return False

while True:
    menu()
    brance = int(input('Введите команду: '))
    if brance == 0:
        print('0. Выход из игры')
        break
    elif brance == 1:
        pole = begin()
        look_pole(pole)
        who = random.choice(GAMERS)
        while True:
            print(f'Ход начинает {who}')
            print(f'{who[0]}-ик, введи: Строку, Графу (поочереди, в виде целого числа от 0 до 2)')
            pole = step(pole, who)
            look_pole(pole)
            if win(pole):
                break
            if check(pole):
                break
            who = list(filter(lambda x: x !=who, GAMERS))[0] # переход хода