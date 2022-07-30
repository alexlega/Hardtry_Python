"""Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
финансовым результатом работает фирма. Например, прибыль — выручка больше издержек,
или убыток — издержки больше выручки. Выведите соответствующее сообщение.

Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение
прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль
фирмы в расчёте на одного сотрудника."""


n = int(input("Please enter the value of proceeds: "))
m = int(input("Please enter the value of outgoings: "))

if n > m:
    rent = n / m
    print("Your company is profitable. Profitability = ", rent)
    num = int(input("Please enter amount of employee: "))
    prof = rent / num
    print("Profitability counting on employ = ", prof)
elif n < m:
    print("Your company is operating at a loss")

