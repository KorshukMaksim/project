print('Задача 9. Игра «Угадай число»')
import random
guesses_made = 0
number = random.randint(1, 7)
while guesses_made < 6:
    guess = int(input('Введи число: '))
    guesses_made += 1
    if guess < number:
        print('Число меньше,чем нужно. Попробуйте еще раз!')
    if guess > number:
        print('Число больше, чем нужно. Попробуйте еще раз!')
    if guess == number:
        break
if number == guess:
    print('Вы угадали! Число попыток:', guesses_made)
else:
    print('А вот и не угадал! Я загадал число ', number)
# В одном из домашних заданий мы делали задачу, 
# где папа-программист написал для сына программу, которая просит его угадать число.
# Недостаток программы был в том, 
# что бедному сыну приходилось её каждый раз перезапускать, чтобы угадывать число. 
# Теперь, когда мы знаем гораздо больше,
# пришло время исправить этот недостаток и заодно немного улучшить саму игру.
 
# Напишите программу-игру,
# которая запрашивает у пользователя число до тех пор,
# пока он его не отгадает.
# Выводите сообщения в соответствии с примером.
 
# Пример (загадали число 7):
# Введите число: 3
# Число меньше, чем нужно. Попробуйте ещё раз!
# Введите число: 10
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 8
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 7
# Вы угадали! Число попыток: 4