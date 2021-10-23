teencode_dict = {
    'stt': 'so thu tu',
    'pt': 'phat trien'
}
running = True
while running:
    for key in teencode_dict:
        print(key, end='\t')
    print()
    input_word = input('your code? ')
    if input_word in teencode_dict:
        print('trans:', teencode_dict[input_word])
    else:
        user_choice = input('your word is not in the dictionary, do you want to contrib?(y/n)')
        if user_choice == 'y':
            word_meaning = input('enter the meaning')
            teencode_dict[input_word] = word_meaning
        else:
            print('bye bye')
            running = False