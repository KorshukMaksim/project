print('Задача 7. Стипендия')
educational_grant = int(input(' Введите размер стипендии: '))
expenses = int(input('Введите расходы: '))
mouth = 10
summ = expenses
for i in range(2, mouth +1):
    expenses = expenses * 1.03
    summ = summ + expenses
    summ2 = (summ - educational_grant * mouth) // 1+1
print('У родителей необходимо попросить:', summ2, 'рублей')
#Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# 
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.