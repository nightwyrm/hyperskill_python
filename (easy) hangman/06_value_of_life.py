import random


options = ('python', 'java', 'kotlin', 'javascript')
word = random.choice(options)
mask = '-' * len(word)
guesses = set()
print('H A N G M A N')
wrong = 0
while wrong != 8:
    print('\n' + mask)
    letter = input('Input a letter: ')
    if letter in word and letter not in guesses:
        guesses.add(letter)
        mask = ''.join(char if char in guesses else '-' for char in word)
    elif letter not in word:
        guesses.add(letter)
        print('No such letter in the word')
        wrong += 1
    elif letter in guesses:
        print('No improvements')
        wrong += 1
    if '-' not in mask:
        print(mask)
        print('You guessed the word!')
        print('You survived!')
        exit()
print('You are hanged!')
