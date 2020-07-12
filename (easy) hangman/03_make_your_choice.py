import random

options = ('python', 'java', 'kotlin', 'javascript')
word = random.choice(options)
print('H A N G M A N')
guess = input('Guess the word: ')
if guess == word:
    print('You survived!')
else:
    print('You are hanged!')
