print('Задача 2. Я стал новым пиратом!')
answer = 0
for pirat in range(10):
    text = input('Введите слово: ')
    if(text == 'Карамба') or (text == 'карамба'):
        answer += 1
print('Кол-во правильных ответов', answer)
#Старому капитану необходимо пополнить команду.
# Но попадут на его корабль только достойные! 
# Он отобрал 10 человек и те, кто из них крикнет слово “Карамба”, попадут на борт.
# 
# Пользователь вводит 10 слов. 
# 
# Напишите программу,
# которая определяет, сколько из них совпадают со словом “Карамба”.
