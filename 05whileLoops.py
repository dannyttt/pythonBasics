# while loop
import random
import math
curr_num = 1
while curr_num < 5:
    print(curr_num)
    curr_num += 1

message = "quit"
while message.lower() != 'quit':
    message = input('enter any messages')
    print(message)
    print('enter quit to exit out')

prompt = '\nTell me something to repeat:'
prompt += '\nEnter "exit" to quit program'
message = 'exit'
while message.lower() != 'exit':
    message = input(prompt)
    print(message)

# using flag
activity = False

while activity:
    print(round(random.random())*10)
    message = input('you want more random numbers?')
    if message.lower() == 'no':
        activity = False

# use break to exit loop
while 0:
    print(round((random.random()*10)))
    message = input('you want more random numberssssss?')
    if message.lower() == 'no':
        break

# continue in loop
num = 20
while num >= 0:
    num -= 1
    if num % 2 == 0 or num < 0:
        continue
    print(num)

# moving items from one list to another
unconfirmed_users = ['lisa', 'mia', 'anna']
confirmed_users = []

while unconfirmed_users:
    curr_user = unconfirmed_users.pop()
    confirmed_users.append(curr_user)
print(confirmed_users)

# removing specific values from a list
pets = ['dog', 'cat', 'bird', 'rabbit', 'goldfish', 'cat', 'cat', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# filling a dictionary with user responses
responses = {}
is_polling = True
while is_polling:
    user = input("what is your name: \n")
    response = input('what is your fav thing to do in spare time: \n')
    responses[user] = response
    repeat = input('would you like to add one more person?\n')
    if repeat.lower() == 'no':
        is_polling = False
print(responses)
