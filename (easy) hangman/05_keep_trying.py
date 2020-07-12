import random


options = ('python', 'java', 'kotlin', 'javascript')
word = random.choice(options)
mask = '-' * len(word)
guesses = set()
print('H A N G M A N')
for n in range(0, 8):
    print('\n' + mask)
    letter = input('Input a letter: ')
    if letter not in word and letter not in guesses:
        print('No such letter in the word')
        guesses.add(letter)
    elif letter in word and letter not in guesses:
        guesses.add(letter)
        mask = ''.join(char if char in guesses else '-' for char in word)
    n += 1
print('\nThanks for playing!')
print("We'll see how well you did in the next stage")
