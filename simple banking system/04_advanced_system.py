import random, sqlite3
 
 
# establish sql connection
def sql_con(sql, flag):
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    cur.execute(sql)
    if flag == 'u':
        conn.commit()
        conn.close()
    elif flag == 's':
        result = cur.fetchone()
        conn.close()
        return result
 
 
# initialise database
def init_db():
    sql_con('''CREATE TABLE IF NOT EXISTS card
             (id integer, number text, pin text, balance integer default 0);''', 'u')
 
 
# validate checksum via Luhn algorithm
def checkLuhn(card_num):
    r = [int(ch) for ch in str(card_num)][::-1]
    return (sum(r[0::2]) + sum(sum(divmod(d*2,10)) for d in r[1::2])) % 10 == 0
 
 
# display main menu
def main_menu():
    print('''1. Create an account
    2. Log into account
    0. Exit''')
 
 
# display account menu
def acct_menu():
    print('''1. Balance
    2. Add income
    3. Do transfer
    4. Close account
    5. Log out
    0. Exit''')
 
 
# generate card number and PIN
def gen_card():
    id_qry = sql_con('SELECT max(id) FROM card;', 's')
    if id_qry[0] is None:
        new_id = 1
    else:
        new_id = id_qry[0] + 1
    while True:
        new_card = '400000' + str(random.randint(0, 9999999999)).zfill(10)
        if checkLuhn(new_card) is True:
            break
    new_pin = str(random.randint(0, 9999)).zfill(4)
    sql_con("INSERT INTO card (id, number, pin) VALUES (" + str(new_id) + ", '" + new_card + "', '" + new_pin + "');", 'u')
    print('Your card has been created.')
    print('Your card number: \n' + new_card)
    print('Your card PIN: \n' + new_pin)
 
 
# account logon
def logon():
    in_card = input('Enter your card number: ')
    in_pin = input('Enter your PIN: ')
    try:
        pin_qry = sql_con("SELECT pin FROM card WHERE number = '" + in_card + "';", 's')
        if pin_qry[0] == in_pin:
            print('You have successfully logged in!')
            return in_card
        else:
            print('Wrong card number or PIN!')
    except:
        print('Wrong card number or PIN!')
 
 
# check account balance
def check_bal(card):
    bal_qry = sql_con("SELECT balance FROM card WHERE number = '" + card + "';", 's')
    return bal_qry[0]
 
 
# add funds to account
def add_funds(card, funds):
    curr_bal = check_bal(card)
    sql_con("UPDATE card SET balance = " + str(curr_bal + funds) + " WHERE number = '" + card + "';", 'u')
    print('Income was added!')
 
 
# transfer funds to another account
def xfr_funds(card):
    print('Transfer')
    tgt_card = input('Enter card number: ')
    if checkLuhn(tgt_card) is False:
        print('Probably you made mistake in the card number. Please try again!')
    elif sql_con("SELECT * FROM card WHERE number = '" + tgt_card + "';", 's') is None:
        print('Such a card does not exist.')
    else:
        amt = int(input('Enter how much money you want to transfer: '))
        card_bal = check_bal(card)
        if amt > card_bal:
            print('Not enough money!')
        else:
            add_funds(tgt_card, amt)
            sql_con("UPDATE card SET balance = " + str(card_bal - amt) + " WHERE number = '" + card + "';", 'u')
            print('Success!')
 
 
# close account
def close_acct(card):
    sql_con("DELETE FROM card WHERE number = '" + card + "';", 'u')
    print('The account has been closed!')
 
 
# main code
init_db()
while True:
    main_menu()
    main_action = input()
    if main_action == '1':
        gen_card()
    elif main_action == '2':
        acct = logon()
        while True:
            acct_menu()
            acct_action = input()
            if acct_action == '1':
                print('Balance: ' + str(check_bal(acct)))
            elif acct_action == '2':
                income = int(input('Enter income: '))
                add_funds(acct, income)
            elif acct_action == '3':
                xfr_funds(acct)
            elif acct_action == '4':
                close_acct(acct)
                break
            elif acct_action == '5':
                print('You have successfully logged out!')
                break
            elif acct_action == '0':
                print('Bye!')
                exit()
    elif main_action == '0':
        print('Bye!')
        exit()
    