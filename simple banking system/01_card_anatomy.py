import random


accts = {}


# display main menu
def main_menu():
    print('1. Create an account\n2. Log into account\n0. Exit')


# display account menu
def acct_menu():
    print('1. Balance\n2. Log out\n0. Exit')


# generate card number and PIN
def gen_card():
    global accts
    new_card = '400000' + str(random.randint(0, 9999999999)).zfill(10)
    new_pin = str(random.randint(0, 9999)).zfill(4)
    accts[new_card] = new_pin
    print('Your card has been created.')
    print('Your card number: \n' + new_card)
    print('Your card PIN: \n' + new_pin)


# account logon
def logon():
    in_card = input('Enter your card number: ')
    in_pin = input('Enter your PIN: ')
    if accts[in_card] == in_pin:
        print('You have successfully logged in!')
    else:
        print('Wrong card number or PIN!')


# main code
while True:
    main_menu()
    main_action = input()
    if main_action == '1':
        gen_card()
    elif main_action == '2':
        logon()
        while True:
            acct_menu()
            acct_action = input()
            if acct_action == '1':
                print('Balance: 0')
            elif acct_action == '2':
                print('You have successfully logged out!')
                break
            elif acct_action == '0':
                print('Bye!')
                exit()
    elif main_action == '0':
        print('Bye!')
        exit()
