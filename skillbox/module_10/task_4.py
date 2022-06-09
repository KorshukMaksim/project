print('Задача 4. Крест')
number = int(input('Введите число: '))
print()
for row in range(number + 1):
    for col in range(number + 1):
        if col == row:
            print('^', end = ' ')
        elif col == -row + number:
            print('^', end = ' ')
        else:
            print(' ', end = ' ')
    print()
# Напишите программу,
# которая выводит на экран крест из символов “^”.
#
# (Символы выводятся по диагоналям воображаемого квадрата.)




# ^        ^
#  ^      ^ 
#   ^    ^  
#    ^  ^   
#     ^^    
#     ^^    
#    ^  ^   
#   ^    ^  
#  ^      ^ 
# ^        ^
