''' В дедуктивной логической игре Бейглз необходимо по подсказкам угадать серкетное число из трех цифр. В ответ на ваши попытки
Игра выдает одну из трех подсказок:
Pico - правильная цифра на неправильном месте
Fermi - правильная цифра на правильном месте
Bagels - нет правильных цифр
10 попыток на угадывание и каждый раз вывод попытки

1) Функция 1:
 - в начале говорит сколько есть попыток
 - на каждой попытке обозначает ее номер и считывает задаваемое число
 - спрашивает в конце о желании поиграть еще раз, если да => повтор функции, нет => выход из функции и сообщение - "Спасибо за игру"
2) Функция загадывания числа 2:
 - входной параметр - разрядность угадываемого числа
3) Функция 3, дающая подсказки:
 - получает на вход секретное число и загадываемое числа
 - в ответ выдает подсказки, согласно условию задачи
'''
import random
from random import randint

tries_number = 5 ## Кол-во попыток для угадывания
count_number = 3 ## Разрядность угадываемого числа

# Функция загадывания секретного числа
def randomnumber(count_number):
    count_number = int(count_number)
    if count_number == 1:
        return randint(0, 9)
    else:
        return randint(10 ** (count_number - 1), int('9' * count_number))

'''Аналог реализации функции загадывания секретного числа
def randomnumber(count_number):
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(count_number):
        secretNum += str(numbers[i])
    return secretNum
'''

def rightdigits(user_number, secretnumber):
    user_number = str(user_number)
    secretnumber = str(secretnumber)
    result = str()
    length = int(len(secretnumber))
    fermi_count = int()
    user_number_cur_symb_index = -1
    for i in user_number:
        user_number_cur_symb_index += 1
        secret_number_cur_symb_index = -1
        for k in secretnumber:
            secret_number_cur_symb_index += 1
            print('i = ' + str(i) + ' k = ' + str(k) + ' user_number_cur_symb_index = ' + str(user_number_cur_symb_index) + ' secret_number_cur_symb_index = ' + str(secret_number_cur_symb_index))
            if i == k and user_number_cur_symb_index == secret_number_cur_symb_index:
                if result == '':
                    result += 'Fermi'
                else:
                    result += ' Fermi'
                fermi_count += 1
                break
            if i == k and user_number_cur_symb_index != secret_number_cur_symb_index:
                if result == '':
                    result += 'Pico'
                else:
                    result += ' Pico'
                break
    if result == '':
        result = 'Bagels'
    elif fermi_count == length:
        result = 'right'
    return result # Сортируем подсказки, чтобы не выдавать исходное положение .sort()

def main():
    secretnumber_for_user = int(randomnumber(count_number))  ## Загадываем число
    print('Это игра Baegls. У вас имеется ' + str(tries_number) + ' попыток для разгадывания числа. Желаю удачи!')
    for i in range(tries_number):
        print('Попытка # ' + str((i + 1)) +':')
        user_try_number = int(input())
        res = rightdigits(user_try_number, secretnumber_for_user)
        if res == 'right':
            print('Вы угадали!. Cыграть еще раз? (Yes/No)')
            user_answer = str(input())
            if user_answer == 'Yes':
                main()
            else:
                print('Игра закончена!')
                break
        else:
            print(res)
    else:
        print('Ваши попытки подошли к концу. Желаете попробовать вновь? (Yes/No)')
        user_answer = str(input())
        if user_answer == 'Yes':
            main()
        else:
            print('Игра завершена!')

 main()
