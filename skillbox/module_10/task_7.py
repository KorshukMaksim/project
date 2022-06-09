print('Задача 7. Наибольшая сумма цифр')


seqNum = int(input('Введите количество чисел: '))
max_m = 0
max_sum =0
summ = 0
for i in range(seqNum):
    print('Введите число: ', end = ' ')
        number:  = int(input())
        this_num = number
        while number > 0:
            summ += number %10
                number //= 10
                    if summ > max_sum:
                     max_sum = summ
                        max_num = this_num
                         summ = 0
print('Число',max_num,'имеет максимальную сумму цифр:', max_sum)
# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.
