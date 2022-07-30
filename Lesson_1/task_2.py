"""Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

sec_time = int(input("Please enter time with seconds: "))
hours = sec_time // 3600
minutes = sec_time // 60 - hours * 60   # convert the total amount of time in minutes and exclude full hour minutes
seconds = sec_time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")