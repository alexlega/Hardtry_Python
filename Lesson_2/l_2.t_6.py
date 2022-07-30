"""*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
элемента — номер товара и словарь с параметрами, то есть характеристиками товара:
название, цена, количество, единица измерения. Структуру нужно сформировать программно,
запросив все данные у пользователя."""
#
goods_exp = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название":"принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]

# l_1 = []
# l_2 = []
# l_3 = []
goods = []
# i = 1

# while True:
#     user = int(input("enter 1 if you want to continue, enter 2 if you want to stop: "))
#     if user == 1:
#         name = input("name: ")
#         cost = int(input("cost: "))
#         amount = int(input("amount: "))
#         goods.append((i, {"name": name, "cost": cost, "amount": amount}))
#         # l_1.append(name)
#         # l_2.append(cost)
#         # l_3.append(amount)
#         i += 1
#     elif user != 1:
#         break

# for (i, product) in goods_exp:
#     print(f'\n\ni: {i}, product: {product}')
#     for k, v in product.items():
#         print(f'i: {i}, k: {k}, v: {v}')


# anal_goods = {"name": l_1, "cost": l_2, "amount": l_3}
# l = []
# anal_goods = goods[0][1].items()
# print(anal_goods)
# print(goods)
# print(f" name: {anal_goods['name']} \n cost: {anal_goods['cost']} \n amount:{anal_goods['amount']}")
