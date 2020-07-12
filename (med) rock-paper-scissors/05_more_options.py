import random


# set up options
def set_options():
    txt = input()
    if not txt:
        lst = ['rock', 'paper', 'scissors']
    else:
        lst = txt.split(',')
    return lst


# load scores from file
def load_scores():
    src_data = {}
    with open('rating.txt', 'r') as f_in:
        for line in f_in:
            (key, val) = line.split()
            src_data[key] = int(val)
    f_in.close()
    return src_data


# check who wins
def compare_guess(in_guess, in_options):
    i = in_options.index(in_guess)
    length = len(in_options)
    move = (i - (length - 1) // 2) % length
    rot_options = in_options[move:] + in_options[:move]
    computer = random.choice(rot_options)
    if in_guess == computer:
        print(f'There is a draw ({computer})')
        result = 'draw'
    elif rot_options.index(in_guess) > rot_options.index(computer):
        print(f'Well done. Computer chose {computer} and failed')
        result = 'win'
    elif rot_options.index(in_guess) < rot_options.index(computer):
        print(f'Sorry, but computer chose {computer}')
        result = 'loss'
    return result


# update user's score
def upd_score(result, curr_score):
    scores = {'win': 100, 'draw': 50, 'loss': 0}
    new_score = curr_score + scores[result]
    return new_score


# main code
filedata = load_scores()
user = input('Enter your name: ')
print(f'Hello, {user}')
if filedata.get(user) is None:
    score = 0
    filedata.update({user: score})
else:
    score = filedata[user]
options = set_options()
print("Okay, let's start")
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
        score = upd_score(compare_guess(guess, options), score)
        filedata[user] = score
