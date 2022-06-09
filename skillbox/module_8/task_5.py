print('Задача 5. Функция 2')
x = int(input('Начало отрезка : '))
a = int(input('Конец отрезка: '))
step = int(input('Шаг: '))
y = 0
for fun in range(a, x - 1, step):
    y = (fun ** 3) + 2 * (fun ** 2) - (4 * fun) + 1
    print('в точке', fun, 'функция равна', y)
#В прошлый раз мы написали Саше программу,
# которая считает функцию в каждой точке отрезка и выводит значение на экран.
# Но теперь ему нужно,
# чтобы значения считались в обратном порядке.
# Плюс к этому в программе ему нужно сделать так,
# чтобы можно было настраивать шаг, с которым он скачет по точкам отрезка.
# 
# Напишите программу,
# которая получает на вход начало и конец отрезка, а также шаг.
# Затем высчитывает функцию игрек в каждой точке отрезка
# и с нужным шагом, начиная с конца, и выводит ответ на экран.

# Сама функция выглядит так:
# y = x**3 + 2x**2 - 4x + 1

# Пример:
# 
# Введите начало отрезка: -2
# Введите конец отрезка: 2
# Введите шаг: -1
# В точке 2 функция равна 9
# В точке 1 функция равна 0
# В точке 0 функция равна 1
# В точке -1 функция равна 6
# В точке -2 функция равна 9