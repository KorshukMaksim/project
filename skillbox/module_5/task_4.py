print('Задача 4. Поступление')

# В университете на особый факультет на направление кибернетики
# очень серьёзный конкурс — поступают только сильнейшие,
# первые десять человек из списка.
# Потом среди поступивших определяется, кто будет на стипендии.
# Для стипендии общий балл при поступлении должен составлять не менее 290.

# Напишите программу,
# которая получает на вход место студента в списке и его балл,
# а затем выводит соответствующие сообщения о поступлении и получении стипендии.

# Пример 1:
# Введите место в списке поступающих: 3
# Введите количество баллов за экзамены: 295
# Поздравляем, Вы поступили!
# Бонусом Вам будет начисляться стипендия

# Пример 2:
# Введите место в списке поступающих: 3
# Введите количество баллов за экзамены: 270
# Поздравляем, Вы поступили!
# Но Вам не хватило баллов для стипендии

# Пример 3:
# Введите место в списке поступающих: 11
# К сожалению, вы не поступили.
mesto = int(input('Введите место в списке поступающих: '))
bal = int(input('Введите количество баллов за экзамены: '))
if mesto <= 10 and bal >= 290:
    print('Поздравляем, Вы поступили!')
    print('Бонусом Вам будет начисляться стипендия')
if mesto <= 10 and bal <= 289:
    print('Поздравляем, Вы поступили!')
    print('Но Вам не хватило баллов для стипендии')
if mesto >10 and bal >= 290:
    print('К сожалению, вы не поступили.')
