print('Задача 5. Модуль числа')
number = int(input(' число: ', ))
if number >= 0:
    print(number)
else:
    var = number < 0
    number_1 = number * (-1)
print(number_1)

# Математик Саша пишет программу, которая должна строить график функции y = |x|.
# Для этого ему нужно находить модуль очередного числа x,
# то есть если число x отрицательное, то переводить его в положительное.
# Напишите программу, которая выводит на экран модуль введённого числа.
#
# Пример:
# Ввели 5, ответ 5
# Ввели −7, ответ 7
#
# Подсказка: достаточно в некоторых случаях переприсвоить переменную со знаком минус.