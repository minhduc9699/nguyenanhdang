mon_an_1 = 'com'
mon_an_2 = 'pho'
mon_an_3 = 'thit cho'

menu = ['com', 'pho', 'thit cho', 'bun', 'bun'] # init

print(menu)
# I C R U D

# Create
menu.append('mam tom')
print(menu)

# Read
# Read all
for i in range(len(menu)):
    print(i+1, menu[i])

for item in menu:
    print(i)

for index, item in enumerate(menu):
    print(index, item)

# Update
menu[2] = 'thit meo'
print(menu)

# Delete
deleted_item = menu.pop(2)
print('deleted_item', deleted_item)
menu.remove('bun')
print(menu)