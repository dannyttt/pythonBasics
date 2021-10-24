alien_0 = {
    'color': 'green',
    'points': 5
}

print(alien_0['color'])
print(alien_0['points'])

# dictionary is a collection of key-value paris.

new_point = alien_0['points']
print(f'you have earned {new_point} points')

# adding key paried values to the dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0 = {}
alien_0['color'] = 'blue'
alien_0['points'] = 10
alien_0['x_position'] = 10
alien_0['y_position'] = 10
alien_0['speed'] = 'fast'
if alien_0['speed'] == 'fast':
    x_increment = 5
elif alien_0['speed'] == 'slow':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(alien_0)

del alien_0['points']
print(alien_0)

fav_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# using get to access values
print(fav_language.get('jens', 'no such person'))

# looping through dictionary
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
# looping through key and values using method .items()
for key, value in user_0.items():
    print(f'key: {key}, value: {value}')
for k, y in fav_language.items():
    print(f'{k.title()}\'s fav lang is {y.title()}')
# looping through key using method .keys(), it can be the default behavior of python, works without .keys()
for name in fav_language.keys():
    print(name)


names = ['phil', 'sarah']

for name in fav_language:
    print(f'Hi, {name}')
    if name in names:
        lang = fav_language[name]
        print(f'{name}, I see you like {lang}')

if 'eric' not in fav_language.keys():
    print('eric was not in poll')

# .keys() returns a list of all keys.
print(fav_language.keys())

# looping through key in particular order
for name in sorted(fav_language.keys()):
    print(f'{name}, thx for taking the poll')

# looping through all values.
for lang in fav_language.values():
    print(lang)
# use set() to return unqiue values in the dictionary
for lang in set(fav_language.values()):
    print(lang)

# nesting dictionary
alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yellow', 'points': '10'}
alien_2 = {'color': 'red', 'points': '15'}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
aliens = []
for el in range(30):
    aliens.append(alien_0)
print(aliens)
print(len(aliens))

for el in aliens[:5]:
    if el['color'] == 'green':
        el['color'] = alien_1['color']
for el in aliens[:5]:
    print(el)

# list inside a dictionary
pizz = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra chess']
}

# loop list inside dictionary
for el in pizz['toppings']:
    print(el)
fav_language = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for k, y in fav_language.items():

    if(len(y) > 1):
        print(f'hello, {k} your fav languages are')
        for lang in y:
            print(lang)
    else:
        print(f'hello, {k} your fav language is')
        for lang in y:
            print(lang)

# dictionary in a dictionary
# ask user input first and last name with locations
users = {
    'dazeng': {
        'first': 'Danny',
        'last': 'Zeng',
        'location': 'Spring'
    },
    'limia': {
        'first': 'Lisa',
        'last': 'Mia',
        'location': 'Spring'
    }
}


def get_user():
    return_users = []
    for k in users:
        return_users.append(k)
    if(return_users == 0):
        return False
    return return_users


def add_user():
    check_len = len(users)
    get_user_id = get_user()
    f_name = input('enter your first name: \n')
    l_name = input('enter your last name: \n')
    location = input('enter your current loction: \n')
    user_id = f_name[:2]+l_name
    if user_id.lower() not in get_user_id:
        users[user_id.lower()] = {'first': f_name,
                                  'last': l_name, 'location': location}
    if(len(users) > check_len):
        print(users[user_id.lower()])
        print('user added successfully')
    else:
        print('failed to add user.')
    return


# add_user()
full_name = users['dazeng']['first']
print(full_name)
print(type(users))
for user_id, value in users.items():
    print(f"full name: {value['first']} {value['last']}")
