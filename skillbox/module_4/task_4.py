print('Задача 4. Калькулятор скидки')
price = int(input('Введите стоймость: ', ))
price_1 = int(input('Введите стоймость: ', ))
price_2 = int(input('Введите стоймость: ', ))
total_cost = (price + price_1 + price_2)
if total_cost > 10000:
    sale = total_cost - (total_cost * 10 / 100)
    print(sale)
else:
    var = total_cost < 10000
    print(total_cost)
# Андрей переехал на новую квартиру, и ему нужно купить три стула в разные комнаты.
# Естественно, цена на стулья в разных магазинах различается,
# а где-то ещё и скидка есть. 
# Вот для одного из таких магазинов он и написал калькулятор скидки, 
# чтобы проще ориентироваться в ценах.
 
# Напишите программу,
# которая запрашивает три стоимости товара и вычисляет сумму чека. 
# Если сумма чека превышает 10 000 рублей,
# то нужно вычесть из этой суммы скидку 10% (умножить на 10, разделить на 100). 
# В конце вывести итоговую сумму на экран.