print('Задача 1. Язык математики')
# Маше для защиты курсовой работы нужно написать программу для расчёта экономической модели по формуле.
# Как записать саму формулу в программу, она не знает, у неё есть только начальные значения.
# Поэтому Маша решила просто заплатить Егору, чтобы тот написал её быстрее.
#
# Дана программа:
# a = 8
# b = 10
# c = 12
# d = 18
#
# Продолжите программу:
# переведите выражение с математического языка на язык Python, запишите его в переменную res и выведите результат.
#
# Выражение:

# (-3 + a**2) * b - 2**3
#      c- 2 * d

a = 8
b = 10
c = 12
d = 18
d_1 = (a**2)
d_2 = (-3+d_1)
d_3 = (d_2*b)
d_4 = (d_3-(2**3))
a_1 = (c-(2*d))
print(d_4)
print(a_1)