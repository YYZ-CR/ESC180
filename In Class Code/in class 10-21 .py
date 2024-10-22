def lookup_users_by_password(passwords, pwd):
    user_list = []
    for user, pwd0 in passwords.items():
        if pwd == pwd0:
            user_list.append(user)
    return user_list


def lookup_user_by_password(passwords, pwd):
    for user, pwd0 in passwords.items():
        if pwd == pwd0:
            return user

if __name__ == '__main__':
    passwords = {'yip': 'coffee', 'bentz': 'milk', 'guerzhoy': 'coffee'}
    print(lookup_user_by_password(passwords, 'water'))
    print(lookup_users_by_password(passwords, 'coffee'))
    print('water' in passwords.values()) #False
    print('yip' in passwords.keys()) # True

