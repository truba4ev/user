account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

User_list = ['user1', 'user2', 'user3', 'user4']

key = input('Введите ключ (name или account): ')
try:
    key = 'NaMe'
    print(f"значение ключа name для юзера 1: {user1['name']}")
    print(f"значение ключа name для юзера 2: {user2['name']}")
    print(f"значение ключа name для юзера 3: {user3['name']}")
    print(f"значение ключа name для юзера 4: {user4['name']}")
except SyntaxError:
    print('Введенный ключ не найден')

number = input('Введите порядковый номер: ')