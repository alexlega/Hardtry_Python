"""Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
input()."""

# my_list = list(input("Please enter something: ").split(","))
# my_list = [1, 2, 3, 4, 5]
#
# for i in range(len(my_list) // 2):
#    my_list[i * 2 + 1], my_list[i * 2] = my_list[i * 2], my_list[i * 2 + 1]
# print(my_list)

# ------------------------------------------------------------------------------------------

# 
# for i in range(1, len(my_list), 2):
#     my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
# 
# print(my_list)

# ------------------------------------------------------------------------------------------

# for i in range(len(my_list) // 2):
#     tmp_el = my_list[i * 2]
#     my_list[i * 2] = my_list[i * 2 + 1]
#     my_list[i * 2 + 1] = tmp_el
# print(my_list)

# ------------------------------------------------------------------------------------------

# 
# for i in range(1, len(my_list), 2):
#     my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
# 
# print(my_list)

# ------------------------------------------------------------------------------------------
#
# a = [1, 2, 3, 4]
# m = []
# if range(len(a) - 1) == 0:
#     for i in a:
#         m.append(a[i + 1])
#         m.append(a[i])
#         print(m)

# ------------------------------------------------------------------------------------------
# class range(start, stop[, step])
# https://docs.python.org/3/library/stdtypes.html?highlight=range#range

# l_f_trade = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# r = range(len(l_f_trade))
# print(range(len(l_f_trade)))
# for i in r[:4]:  # setting a breakpoint is not an ultimatum solution
#     v = l_f_trade[i * 2]
#     l_f_trade[i * 2] = l_f_trade[i * 2 + 1]
#     l_f_trade[i * 2 + 1] = v
#     print(i)
# print(l_f_trade)
