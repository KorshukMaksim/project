print('Задача 6')
# Реализуйте программу,
# которая запрашивает два числа у пользователя.
# После этого у каждого числа возьмите две последние цифры.
# Получившиеся два числа сложите и выведите на экран.

# Пример:
# Введите первое число: 456
# Введите второе число: 123
# Сумма: 79
a = int(input("число 1:"))
b = int(input("число 2:"))
e = int(a % 100)
f = int(b % 100)
j = int(e+f)
print(j)
