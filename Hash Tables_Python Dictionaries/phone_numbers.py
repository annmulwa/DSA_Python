phone_numbers = {
    'mary' : '12345',
    'john' : '67891',
    'paul' : '34567'
}
print(phone_numbers)

# view the value of a key in a dictionary
print(phone_numbers['mary'])

# Add a new value
phone_numbers['stacy'] = '56789'

# update an existing value
phone_numbers['mary'] = '23456'

# view updated dictionary
print(phone_numbers)

# loop over the phone numbers
for name in phone_numbers:
    print('Name:', name, ', Phone Number:', phone_numbers[name])