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
