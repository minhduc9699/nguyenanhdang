shop = ['ao phong', 'ao dai']

while True:
    action = input('Welcome to our shop, what do you want? (C R U D): ').lower()
    if action == 'c':
        new_item = input('enter new item: ')
        shop.append(new_item)
    elif action == 'r':
        for index, item in enumerate(shop):
            print(index + 1, item)
    elif action == 'u':
        update_index = int(input('enter index: '))
        new_item = input('enter new item')
        shop[update_index - 1] = new_item
    elif action == 'd':
        delete_index = int(input('enter index: '))
        shop.pop(delete_index - 1)
    else:
        print('what do mean??')
    print(shop)