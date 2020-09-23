account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

User_list = [user1, user2, user3, user4]

#user1 = user[0]
#user2 = user[1]
#user3 = user[2]
#user4 = user[3]

key = input('Введите ключ (name или account): ')
if key == 'NaMe':
    print(f"значение ключа name для юзера 1: {user1['name']}")
    print(f"значение ключа name для юзера 2: {user2['name']}")
    print(f"значение ключа name для юзера 3: {user3['name']}")
    print(f"значение ключа name для юзера 4: {user4['name']}")
else:
    print('Введенный ключ не найден')

number = int(input('Введите порядковый номер: '))

if number == 1:
    print(f"имя: {user1['name']}")
    print(f"возраст: {user1['age']}")
    print(f"Логин: {account1['login']}")
    print(f"Пароль: {account1['password']}")
else:
    number == 2
    print(f"имя: {user2['name']}")
    print(f"возраст: {user2['age']}")
    print(f"Логин: {account2['login']}")
    print(f"Пароль: {account2['password']}")
elif:
    number == 3
    print(f"имя: {user3['name']}")
    print(f"возраст: {user3['age']}")
    print(f"Логин: {account3['login']}")
    print(f"Пароль: {account3['password']}")
elif:
    number == 4
    print(f"имя: {user4['name']}")
    print(f"возраст: {user4['age']}")
    print(f"Логин: {account4['login']}")
    print(f"Пароль: {account4['password']}")
else:
    number > 4
    print('Нет такой карточки')