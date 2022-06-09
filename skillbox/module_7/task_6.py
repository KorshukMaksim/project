print('Задача 6. Успеваемость в классе')
class_student = int(input('Введите количество человек вклассе: '))
exelent = 0
good = 0
bad = 0
for grade in range(1, class_student + 1):
    grade_student = int(input('Введите оценку ученика от 3 до 5: '))
while grade_student > 5 or grade_student < 3:
    print('Вы ввели оценку выше 5 или меньше 3. Повторите ввод оценки')
    grade_student = int(input('Введите оценку ученика от 3 до 5: '))
if grade_student == 5:
    exelent += 1
if grade_student == 4:
    good += 1
if grade_student == 3:
    bad += 1
if exelent > good and exelent > bad:
    print('Сегодня лидируют отличники')
if good > exelent and good > bad:
    print('Сегодня лидируют хорошисты')
if bad > exelent and bad > good:
    print('Сегодня лидируют троечники')
if exelent == good and exelent > bad:
    print('Сегодня отличников и хорошистов ровное кол-во')
if exelent == bad and exelent > good:
    print('Сегодня отличников и троечников ровное кол-во')
if bad == good and bad > exelent:
    print('Сегодня троечников и хорошистов ровное кол-во')
if exelent == good and exelent == bad:
    print('Сегодня у всех учеников равное кол-во оценок')
# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. 
# 
# Напишите программу, 
# которая получает список оценок - N чисел - и выводит на экран сообщение о том, 
# кого сегодня больше: отличников, хорошистов или троечников.