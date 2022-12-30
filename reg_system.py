import json
from os import system


with open('user.json', 'r') as userFile:
    users: list[dict] = json.load(userFile)


def clear():
    system('cls')


def check_user_input(user: str, password: str) -> bool:
    msg = 'Usuário ou Senha inválida.\n'

    def check_username(user):
        for u in users:
            if user == u['usr']:
                clear()
                print('Usuário já utilizado.\n')
                return True
        return False

    if user.isspace() or password.isspace():
        clear()
        print(msg)
        return True
    if user == '' or password == '':
        clear()
        print(msg)
        return True
    if user == password:
        clear()
        print(msg)
        return True
    return check_username(user)


while True:
    user = input('user: ')
    password = input('password: ')

    if not check_user_input(user, password):
        break


with open('user.json', 'w') as userFile:
    users.append({'usr': user, 'psw': password})
    json.dump(users, userFile, indent=2)

if __name__ == '__main__':
    with open('user.json', 'r') as userFile:
        f = json.load(userFile)

    print(f)
