"""Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и dict"""


user = int(input("Please enter the number of month: " ))
seasons = {"Winter": [1, 2, 12], "Spring": [3, 4, 5], "Summer": [6, 7, 8], "Autumn": [9, 10, 11]}

if user in sum(seasons.values(), []):   # merge all values(lists) in one list

    for i in seasons.items():   # seasons.items() = merge each value, key in tuple, making 4 tuples
        if user in i[1]:      # in each tuple looking for user`s number
            print(i[0])       # if number exist in any tuple = print 1st tuple`s variable

elif user != sum(seasons.values(), []):
    print("There is no such month")

# seasons = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer", 7: "summer", 8: "summer",
#      9: "autumn", 10: "autumn", 11: "autumn", 12: "winter"}
#
# print(a.get(user))