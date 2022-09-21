# Создайте программу для игры с конфетами человек против человека.

from random import randint

def player():
    candies_total = 2021
    max_take = 28
    count = 0
    player_One = input("\nВведите имя первого игрока: ")
    player_Two = input("\nВведите имя второго игрока: ")

    print("\nДля начала опеределим кто первый начнет игру.\n")

    x = randint(1, 2)
    if x == 1:
        lucky = player_One
        loser = player_Two
    else:
        lucky = player_Two
        loser = player_One
    print(f"Поздравляю {lucky}, ты ходишь первым! ")

    while candies_total > 0:
        if count == 0:
            step = int(input(f"\n{lucky}: "))
            if step > candies_total or step > max_take:
                step = int(input(
                    f"\nМожно взять только {max_take} конфет. {lucky}, попробуй еще раз: "))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f"\nНа кону еще {candies_total}")
            count = 1
        else:
            print("Конфет нет")

        if count == 1:
            step = int(input(f"\n{loser}: "))
            if step > candies_total or step > max_take:
                step = int(input(
                    f"\nМожно взять только {max_take} конфет. {loser}, попробуй еще раз: "))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f"\nНа кону еще {candies_total}")
            count = 0
        else:
            print("Конфет нет")
    
    if count == 1:
        print(f'{loser} ТЫ ПОБЕДИЛ')
    if count == 0:
        print(f'{lucky} ТЫ ПОБЕДИЛ')
    
player()



def player_bot():
    candies_total = 2021
    max_take = 28
    player_One = input("Введите имя игрока: ")
    player_Two = "Компьютер"
    players = [player_One, player_Two]
    print("\nДля начала опеределим кто первый начнет игру.\n")

    lucky = randint(-1, 0)

    print(f"Поздравляю {players[lucky+1]} ты ходишь первым!")

    while candies_total > 0:
        lucky += 1

        if players[lucky % 2] == "Компьютер":
            print(f"\nХодит {players[lucky%2]} \nНа кону : {candies_total} ")

            if candies_total < 29:
                step = candies_total
            else:
                delenie = candies_total//28
                step = candies_total - ((delenie*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\nНу чтож ходи,  {players[lucky%2]}. \nНа кону : {candies_total} '))
            while step > max_take or step > candies_total:
                step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз! '))
        candies_total = candies_total - step

    print(f'На кону осталось {candies_total}. \nПобедил {players[lucky%2]}')

player_bot()