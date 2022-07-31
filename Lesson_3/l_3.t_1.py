'''#1 Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль.'''

def my_func(x1, x2):
    # x1 = float(input('Vvedite pervoe chislo:'))
    # x2 = float(input('Vvedite vtoroe chislo:'))
    try:
        c = x1 / x2
    except ZeroDivisionError:
        return
    return c


print(my_func(10,10))
