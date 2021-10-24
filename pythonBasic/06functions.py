def greet_user(user):
    print(f'hello, {user}')


# user = input('enter your name: \n')
# greet_user(user)

# function return dictionary
person = {}


def return_dic(first, last, age=None):
    person['first'] = first
    person['last'] = last
    if age:
        person['age'] = age
    return


def unpack_dic():
    return f"{person['first']} {person['last']}"


new_person = return_dic('lisa', 'mia', 16)
# print(new_person)

while 0:
    f_name = input('enter first name: \n')
    print('enter q at any time to quit')
    if f_name.lower() == 'q':
        break
    l_name = input('enter last name: \n')
    if f_name.lower() == 'q':
        break
    return_dic(f_name, l_name)
    full_name = unpack_dic(f_name, l_name)
    print(f'full name: {full_name}')

uncompleted_designs = ['phone case', 'phone screen protector', 'air pod']
completed_designs = []


def print_model(com, uncom):
    while uncom:
        curr_val = uncom.pop()
        com.append(curr_val)


def completed(complete):
    for el in complete:
        print(el)


print_model(completed_designs, uncompleted_designs[:])

completed(completed_designs)
print(uncompleted_designs)

# arbitrary number of arguments

# *toppings make empty tuple
# arbitrary arugment must be placed last with other arguments


def make_pizza(*toppings):
    print(toppings)


make_pizza('pepperoni', 'mushrooms', 'green peppers', 'extra cheese')

# **user_info


def create_user(first_name, last_name, **user_info):
    user_info['first'] = first_name
    user_info['last'] = last_name
    return user_info


new_user = create_user('Lisa', 'Mia', location='Spring',
                       field='Computer science')
print(new_user)
