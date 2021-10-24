inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['gammar doppler', 'dagger', 'bedroll', 'bayonet']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']

inventory['backpack'].pop(1)
inventory['gold'] = inventory['gold'] + 50
print(inventory)

