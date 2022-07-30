"""Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""

n = 926938013
m = 0

while n > 0:
    v = n % 10
    n = n // 10

    print(f'n: {n}, v: {v}')

    if v > m:
        m = v

print(m)


# print(
#     'Max: {}'.format(max(map(int, n)))
# )
#
# m = 0
# for el in n:
#     el_int = int(el)
#     if m < el_int:
#         m = el_int

# i = 0
#
# while i < len(n):
#     v = n[i]
#     print(v)
#     i += 1

# print()
