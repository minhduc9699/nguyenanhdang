person = ['Duc', 21, 175, 70, False, 'dev']

person = { # dictionary, object
    'name': 'Duc', # key, value
    'age': [

    ],
    'height': {},
    'weight': 70,
    'married': False,
    'job': 'dev',
} 
# container C R U D
print(person['age'])
for key in person:
    print(key, person[key])
# Create
person['hobbie'] = 'rick roll'
print(person)

# Update
person['age'] = 51
print(person)

# delete
del person['age']
print(person)

if 'key' in dictionary:
    ...