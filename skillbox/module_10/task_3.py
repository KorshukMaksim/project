print('Задача 3. Рамка')
a = int(input('Введите высоту рамки: '))
b = int(input('Введите ширину арки: '))

for row in range(a + 1):
    for col in range(b + 1):
        if col == 0 or col == b:
            print('|', end=' ')
        elif row == 0 or row == a:
            print('-', end=' ')
        else:
            print(' ', end=' ')
    print()
# Напишите программу,
# которая рисует с помощью символьной графики прямоугольную рамку.
# Для вертикальных линий используйте символ вертикального штриха “|”,
# а для горизонтальных - дефис “-”. Пусть пользователь вводит ширину и высоту рамки.

#  _ _ _ _ _ _ _ _ _
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |_ _ _ _ _ _ _ _ _|