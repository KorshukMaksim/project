print('Задача 9. В обратном порядке')
# Реализуйте программу,
# которая получает на вход четырёхзначное число и выводит его на экран в обратном порядке.
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных.
# Пример ввода: 1234.
# Пример вывода: 4321.

number = int(input("число 1:"))
a = number // 1000
b = number // 100 % 10
c = number % 100 // 10
d = number % 10
rev_number = d * 1000 + c * 100 + b * 10 + a
print(rev_number)
