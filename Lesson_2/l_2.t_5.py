"""Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
должен разместиться после них."""

ranked = int(input("Please enter natural number: "))
my_ranked = [7, 5, 3, 3, 2]

# for i, el in enumerate(my_ranked):
#     if ranked > el:
#         my_ranked.insert(i, ranked)
#         break
#     elif ranked == el:
#         my_ranked.insert(i + 1, ranked)
#         break
      elif ranked < my_ranked[-1]:
          my_ranked.append(ranked)
          break
#     else:
#         continue
#       
# print(my_ranked)

for i in range(len(my_ranked)):
    if ranked > my_ranked[i]:
        my_ranked.insert(i, ranked)
        break
    elif ranked == my_ranked[i]:
        my_ranked.insert(i, ranked)
        continue
    elif ranked < my_ranked[-1]:
        my_ranked.append(ranked)
        break
    else:
        continue
print(my_ranked)
