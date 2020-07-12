import random

options = ('python', 'java', 'kotlin', 'javascript')
word = random.choice(options)
hint = word[:3] + '-' * len(word[3:])
print('H A N G M A N')
guess = input(f'Guess the word {hint}: ')
if guess == word:
    print('You survived!')
else:
    print('You are hanged!')
