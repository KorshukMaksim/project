print('Задача 10. Максимальное число (по желанию)')
a = int(input('Число 1: ', ))
b = int(input('Число 2: ', ))
c = int(input('Число 3: ', ))
if a > b:
    maximum = a
else:
    maximum = b
    if c>maximum:
        maximum = c
    print('максимальное число', maximum)
# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно 