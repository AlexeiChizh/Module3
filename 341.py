import json

data = {'login': 'psw'}
with open('reg.json', 'a') as f:
   json.dump(data, f)


def reg(login, psw):
    with open('reg.json', 'r') as f:
        data = json.load(f)
    if login in data.keys():
        print('Данный логин уже существует. Придумайте новый логин.')
    else:
        data[login] = psw
        with open('reg.json', 'w') as f:
           json.dump(data,f)
        print(' Регистрация прошла успешно!')

def log_in(login, psw):
    with open('reg.json', 'r') as f:
        data = json.load(f)
    if (login, psw) not in data.items():
        print(' Такого логина или пароля не существует!')
    else:
        print(' Успешный вход!!!')

while True:
    break_point = input('СТОП?   ')
    if break_point == 'да':
        break
    q = input('Вход или регистрация?   ')

    if q == 'вход':
        login = input('Введите логин:   ')
        psw = input('Введите пароль:   ')
        log_in(login, psw)

    elif q == 'регистрация':
        login = input('Введите логин:   ')
        psw = input('Введите пароль:   ')
        reg(login, psw)
