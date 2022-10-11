# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
from random import *
user1 = input('Введите имя первого игрока: ')
user2 = input('Введите имя второго игрока: ')
tern = bool(randint(0, 2))
if tern:
    print(f'Начинает игру {user1}')
else:
    print(f'Начинает игру {user2}')

candys = 100
while candys > 0:
    print('Осталось конфет: ', candys)
    if tern:
        candys -= int(input(f'Ходит {user1}: '))
        tern = not tern
    else:
        candys -= int(input(f'Ходит {user2}: '))
        tern = not tern
if tern:
    print(f'Победил {user2}')
else:
    print(f'Победил {user1}')
print("Игра окончена!")


# a) Добавьте игру против бота
user1 = input('Введите имя игрока: ')

tern = bool(randint(0, 2))
if tern:
    print(f'Начинает игру {user1}')
else:
    print(f'Начинает игру бот')

candys = 100
while candys > 0:
    print('Осталось конфет: ', candys)
    if tern:
        candys -= int(input(f'Ходит {user1}: '))
        tern = not tern
    else:
        print('Ходит бот')
        candys -= randint(0, 29)
        tern = not tern
if tern:
    print(f'Победил бот')
else:
    print(f'Победил {user1}')
print("Игра окончена!")


# b) Подумайте как наделить бота ""интеллектом""
user1 = input('Введите имя игрока: ')

tern = bool(randint(0, 2))
if tern:
    print(f'Начинает игру {user1}')
else:
    print(f'Начинает игру бот')

candys = 100
while candys > 0:
    print('Осталось конфет: ', candys)
    if tern:
        candys -= int(input(f'Ходит {user1}: '))
        tern = not tern
    else:
        print('Ходит бот')
        if candys > 70:
            candys -= randint(0, 29)
        elif 30 < candys < 70:
            candys -= randint(0, 15)
        elif candys < 30:
            candys -= randint(0, 10)

        tern = not tern
if tern:
    print(f'Победил бот')
else:
    print(f'Победил {user1}')
print("Игра окончена!")