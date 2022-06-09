print('Задача 6. Письмо')
side = int(input('Введите 1 сторону письма: '))
side2 = side
envelope = 12
additions = 0
while envelope < side or envelope < side2:
    if envelope < side:
        additions += 1
        side = side / 2
        if envelope < side2:
            additions += 1
            side2 = side2 / 2
print('Складывать', additions, 'раз.')
# У нас есть
# квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт.
# 
# Напишите программу,
# которая подскажет сколько раз нужно сложить письмо пополам,
# чтобы оно поместилось в конверт.
# Размеры письма вводятся с клавиатуры.