import random


# check who wins
def compare_guess(in_guess, in_computer):
    beats = {'rock':'scissors', 'scissors':'paper', 'paper':'rock'}
    if in_guess == in_computer:
        print('There is a draw (' + in_guess + ')')
    elif beats[in_guess] == in_computer:
        print('Well done. Computer chose ' + in_computer + ' and failed')
    elif beats[in_computer] == in_guess:
        print('Sorry, but computer chose ' + in_computer)


# main code
options = ('rock', 'paper', 'scissors')
while True:
    guess = input()
    if guess == '!exit':
        print('Bye!')
        exit()
    elif guess not in options:
        print('Invalid input')
    else:
        computer = random.choice(options)
        compare_guess(guess, computer)
