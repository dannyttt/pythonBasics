magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title())
for magician in magicians:
    print(f'{magician}, that was a great trick\ncan\'t wait to see your next trick, {magician}')

# making Numerical lists using for range loop\
# range() has off by one behavior
for value in range(1, 5):
    print(value)
for value in range(1, 6):
    print(value)
# use range to make a list of numbers
numbers = list(range(1, 6))
print(numbers)
numbers = list(range(2, 11, 2))
print(numbers)
squares = []
for value in range(1, 11):
    # value = value**2
    squares.append(value**2)
print(squares)
print(max(squares))
print(min(squares))
print(sum(squares))

# list comperhensions
squares = [value**2 for value in range(1, 11)]
print(squares)

for val in range(1, 21):
    print(val)
numbers = list(range(1, 1000000))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

odd_number = list(range(1, 10, 2))
print(odd_number)
for num in odd_number:
    print(num)

numbers = list(range(3, 31, 3))
for num in numbers:
    print(num)

cubic_numbers = [num**3 for num in range(1, 10)]
for num in cubic_numbers:
    print(num)

# slicing list
# python stops one item before the second index you specify.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[1:3])
# if you omit the first index in a slice, python automatically starts your slice at the beginning of the list
print(players[:4])
print(players[2:])
# print the last three player from the list
print(players[-3:])
# looping through a slice
for el in players[:3]:
    print(el.title())

# copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('McNuggets')
friend_foods.append('Ice Cream')
# copy to a different address
print(my_foods, my_foods.__add__)
print(friend_foods, friend_foods.__add__)

# Tuples
