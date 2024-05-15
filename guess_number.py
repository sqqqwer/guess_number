from random import randint

computer_choise = randint(1, 100+1)

player_choise = 0
attempts = 0

print('Угадайте число от 1 до 100!\n')

while player_choise != str(computer_choise):
    player_choise = input('Введите число: ')
    try:
        int(player_choise)
    except Exception:
        print('Можно указывать только цифры!')
        continue

    if int(player_choise) > computer_choise:

        print('Ваше число больше того, что загадано')
    elif int(player_choise) < computer_choise:
        print('Ваше число меньше того, что загадано')
    else:
        print('Отличная интуиция! Вы угадали число :)')
    attempts += 1

print(f'Вам понадобилось {attempts} попыток!')
