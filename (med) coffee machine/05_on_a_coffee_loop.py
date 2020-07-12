water = 400
milk = 540
beans = 120
cups = 9
money = 550
espresso = [250, 0, 16, -4, 1]
latte = [350, 75, 20, -7, 1]
cappuccino = [200, 100, 12, -6, 1]


def stock():
    print('\nThe coffee machine has: ')
    print(str(water) + ' of water')
    print(str(milk) + ' of milk')
    print(str(beans) + ' of coffee beans')
    print(str(cups) + ' of disposable cups')
    print('$' + str(money) + ' of money\n')


def buy():
    global water, milk, beans, beans, cups, money
    coffee = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')
    if coffee == '1':
        make_coffee(espresso)
    elif coffee == '2':
        make_coffee(latte)
    elif coffee == '3':
        make_coffee(cappuccino)


def make_coffee(coffee_type):
    global water, milk, beans, beans, cups, money
    if (water // coffee_type[0]) < 1:
        print('Sorry, not enough water!\n')
    elif coffee_type[1] != 0 and (milk // coffee_type[1]) < 1:
        print('Sorry, not enough milk!\n')
    elif (beans // coffee_type[2]) < 1:
        print('Sorry, not enough coffee beans!\n')
    elif (cups // coffee_type[4]) < 1:
        print('Sorry, not enough disposable cups!\n')
    else:
        print('I have enough resources, making you a coffee!\n')
        water -= coffee_type[0]
        milk -= coffee_type[1]
        beans -= coffee_type[2]
        money -= coffee_type[3]
        cups -= coffee_type[4]


def fill():
    global water, milk, beans, beans, cups, money
    in_water = int(input('\nWrite how many ml of water do you want to add:\n'))
    water += in_water
    in_milk = int(input('Write how many ml of milk do you want to add:\n'))
    milk += in_milk
    in_beans = int(input('Write how many grams of coffee beans do you want to add:\n'))
    beans += in_beans
    in_cups = int(input('Write how many disposable cups of coffee do you want to add:\n'))
    cups += in_cups


def take():
    global money
    print('\nI gave you $' + str(money))
    money = 0


action = ''
while action != 'exit':
    action = input('Write action (buy, fill, take, remaining, exit):\n')
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    elif action == 'remaining':
        stock()
