print('Задача 9. Выражение')
x = int(input('Введите число Х:'))
znam = 1
a = 1
b = 0
chisl = 1
res = 1
for i in range(1, 7):
    a = a * 2
    b = a - 1
    chisl = chisl * (x-b)
    znam = znam * (x-a)
    if znam == 0:
        print('некорректное значение Х на 0 делить нельзя')
    else:
        res =chisl/znam
        print('res равно', res)

#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64)) 