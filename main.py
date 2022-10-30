import requests as requests

# First level: Напишите программу, которая выполняет GET-запрос к API с помощью библиотеки requests
# и выведит с помощью f-строк информацию о пользователе (ИМЯ, ФАМИЛИЯ, EMAIL).
result = requests.get('https://reqres.in/api/users/2')

firstName = result.json()['data']['first_name']
lastName = result.json()['data']['last_name']
email = result.json()['data']['email']
print(f'First name : {firstName}, \nLast name: {lastName},\nEmail; {email}')



