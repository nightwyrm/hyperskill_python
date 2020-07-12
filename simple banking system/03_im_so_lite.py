import random, sqlite3
 
 
# establish sql connection
def sql_con(sql, flag):
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    print(sql)
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
    print('1. Create an account\n2. Log into account\n0. Exit')
 
 
# display account menu
def acct_menu():
    print('1. Balance\n2. Log out\n0. Exit')
 
 
# generate card number and PIN
def gen_card():
    id_chk = sql_con('SELECT max(id) FROM card;', 's')
    if id_chk[0] is None:
        new_id = 1
    else:
        new_id = id_chk[0] + 1
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
        db_pin = sql_con("SELECT pin FROM card WHERE number = '" + in_card + "';", 's')
        print(db_pin)
        if db_pin[0] == in_pin:
            print('You have successfully logged in!')
        else:
            print('Wrong card number or PIN!')
    except:
        print('Wrong card number or PIN!')
 
 
# main code
init_db()
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
