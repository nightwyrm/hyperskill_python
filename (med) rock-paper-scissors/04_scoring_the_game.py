import random


options = ('rock', 'paper', 'scissors')
filename = 'rating.txt'


# load scores from file
def load_scores():
    src_data = {}
    with open(filename, 'r') as f_in:
        for line in f_in:
            (key, val) = line.split()
            src_data[key] = int(val)
    f_in.close()
    return src_data


# check who wins
def compare_guess(in_guess, in_computer):
    rules = {'rock':'scissors', 'scissors':'paper', 'paper':'rock'}
    if in_guess == in_computer:
        print(f'There is a draw ({in_computer})')
        result = 'draw'
    elif rules[in_guess] == in_computer:
        print(f'Well done. Computer chose {in_computer} and failed')
        result = 'win'
    elif rules[in_computer] == in_guess:
        print(f'Sorry, but computer chose {in_computer}')
        result = 'loss'
    return result


# update user's score
def upd_score(result, curr_score):
    scores = {'win':100, 'draw':50, 'loss':0}
    new_score = curr_score + scores[result]
    return new_score


# main code
filedata = load_scores()
user = input('Enter your name: ')
print(f'Hello, {user}')
if filedata.get(user) is None:
    score = 0
    filedata.update({user:score})
else:
    score = filedata[user]
while True:
    guess = input()
    if guess == '!exit':
        print('Bye!')
        exit()
    if guess == '!rating':
        print(f'Your rating: {filedata[user]}')
    elif guess not in options:
        print('Invalid input')
    else:
        computer = random.choice(options)
        score = upd_score(compare_guess(guess, computer), score)
        filedata[user] = score
