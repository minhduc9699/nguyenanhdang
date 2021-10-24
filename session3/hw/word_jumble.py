from random import shuffle, choice
words = ['champion', 'loser', 'good game']
word = choice(words)
list_word = list(word)
shuffle(list_word)
print(*list_word)
answer = input('your answer: ')
if answer == word:
    print('hao han')
else:
    print('not hao han')