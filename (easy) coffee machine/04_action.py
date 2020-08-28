water = 400
milk = 540
beans = 120
cups = 9
money = 550

def stock():
    print('The coffee machine has: ')
    print(str(water) + ' of water')
    print(str(milk) + ' of milk')
    print(str(beans) + ' of beans')
    print(str(cups) + ' of disposable cups')
    print(str(money) + ' of money')

def buy():
    global water, milk, beans, beans, cups, money
    coffee = int(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: '))
    if coffee == 1:
        water = water - 250
        beans = beans - 16
        money = money + 4
        cups = cups - 1
    elif coffee == 2:
        water = water - 350
        milk = milk - 75
        beans = beans - 20
        money = money + 7
        cups = cups - 1
    elif coffee == 3:
        water = water - 200
        milk = milk - 100
        beans = beans - 12
        money = money + 6
        cups = cups - 1
    stock()

def fill():
    global water, milk, beans, beans, cups, money
    in_water = int(input('Write how many ml of water do you want to add:'))
    water = water + in_water
    in_milk = int(input('Write how many ml of milk do you want to add:'))
    milk = milk + in_milk
    in_beans = int(input('Write how many grams of coffee beans do you want to add:'))
    beans = beans + in_beans
    in_cups = int(input('Write how many disposable cups of coffee do you want to add:'))
    cups = cups + in_cups
    stock()

def take():
    global money
    print('I gave you $' + str(money))
    money = 0
    stock()

stock()
action = input('Write action (buy, fill, take) : ')
if action == 'buy':
    buy()
elif action == 'fill':
    fill()
elif action == 'take':
    take()
