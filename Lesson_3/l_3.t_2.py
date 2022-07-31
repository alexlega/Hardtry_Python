'''#2 Выполнить функцию, которая принимает несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Осуществить вывод данных о
пользователе одной строкой.'''

def my_inf():
     name = str(input('Vvedite imya:'))
     surname = str(input('Vvedite familiyu:'))
     year = int(input('Vvedite god rojdeniya:'))
     town = str(input('Vvedite gorod:'))
     mail = str(input('Vvedite pochty:'))
     phone = str(input('Vvedite nomer telefona'))
     print(f"name - {name}; surname - {surname}; year - {year}; town - {town}; mail - {mail}; phone - {phone}")
     return name, surname, year, town, mail, phone
    

print(f"name - {name}; surname - {surname}; year - {year}; town - {town}; mail - {mail}; phone - {phone}")
