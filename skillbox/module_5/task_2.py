print('Задача 2. Максимум из трёх чисел')

# Как-то у нас уже было задание 
# на нахождение максимума из трёх чисел с помощью дополнительной переменной.
# Теперь, когда вы знаете намного больше,
# вы можете оптимизировать программу, не тратя память компьютера на лишние переменные.

# Напишите программу,
# которая находит максимум из трёх чисел, не используя дополнительные переменны
a = int(input('Число 1: ', ))
b = int(input('Число 2: ', ))
c = int(input('Число 3: ', ))
if a > b:
    print(a) if a > c else print(c)
else:
    print(b) if b > c else print(c)
