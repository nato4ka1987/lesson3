'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
'''

def my_func(**kwargs):
    return f"{kwargs['name']} {kwargs['surname']} ({kwargs['yearofbirth']}) {kwargs['city']} {kwargs['email']} {kwargs['phone']}"
    user_name = input("Имя>>>")
    user_surname = input("Фамилия>>>")
    user_yearofbirth = int(input("Годрождения>>>"))
    user_city = input("Город>>>")
    user_email = input("Email>>>")
    user_phone = input("Телефон>>>")
    print(my_func(name=user_name, surname=user_surname, yearofbirth=user_yearofbirth, city=user_city, email=user_email, phone=user_phone))
