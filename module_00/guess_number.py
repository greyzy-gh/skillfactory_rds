#! python3
# guess_number.py - укадывает случайное число за минимальное количество попыток
# Проект 0. GitHub. Быстрый старт, секция 0.6

import numpy as np
#=============================================
#number_secret = np.random.randint(1,101)
# print(number_secret)

#=============================================
# Задаем счетчик и начальные условия диапазона
#count = 0
#left, right = 1, 100
#=============================================
# идем по пути отбрасывания половины
#while True:
#    current = (left+right)//2
#    if number == current:
#        break
#    elif number > current:
#        left = current + 1
#    else:
#        right = current - 1
#    count +=1

#=============================================
# Заворачиваем решение в функцию
def game_core_v1(number):
    '''number=np.random.randint(1,101)
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    left, right = 1, 100
    while True:
        current = (left+right)//2
        if number == current:
            break
        elif number > current:
            left = current + 1
        else:
            right = current - 1
        count +=1
    return count

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, за какое количество попыток в среднем угадывает число'''
    # Создаем список, куда запишем количество попыток для угадывания
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    # Угадывать будем из массива, заполненного числами из диапазона 1-100, тысяча чисел
    random_array = np.random.randint(1,101, size=(1000))
    # для каждого числа из массива (случайного) применяем функцию для угадывания
    for number in random_array:
        count_ls.append(game_core(number))
    # вычисляем среднее (sum(count_ls)/len(count_ls))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_core_v1)