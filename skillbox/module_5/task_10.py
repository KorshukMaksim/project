print('Задача 10. Почта')

# Почтовое отделение открывается в 08:00 и закрывается в 22:00.
# С 14:00 до 15:00 все сотрудники уходят на обед,
# а в 10:00 и 18:00 приезжают машины с посылками,
# и тогда все сотрудники на два часа заняты их разгрузкой.
# Во время обеда, разумеется, посылки никто не выдаёт,
# как и в моменты, когда разгружаются машины.

# Напишите программу,
# которая получает на вход время в часах — число от 0 до 23 — и пишет,
# можно ли в этот час получить посылку.
# Используйте только один условный оператор if-else, без elif и прочего.

# Решите задание двумя способами:

# первый — при выполнении условия выводится сообщение:
# «Можно получить посылку»,

# второй —  при выполнении условия выводится сообщение:
# «Посылку получить нельзя».


print('Вариант 1')
hour = int(input('Во сколько приходите?'))
if (hour >= 8 and hour < 10) or (hour >= 12 and hour < 14) or (hout >= 15 and hour < 18) or (hour >= 20 and < 22):
    print('Mожно получить посылку')
else:
    print('Посылку получить нельзя')

print('Вариант 2')
hour = int(input('Во сколько приходите?'))
if (hour >= 0 and hour < 8) or (hour >= 10 and hour < 12) or (hout >= 14 and hour < 15) or (hour >= 18 and hour<= 20) or (hour >=22 and hour <= 24):
    print('Посылку получить нельзя')
else:
    print('Можно получить посылку')