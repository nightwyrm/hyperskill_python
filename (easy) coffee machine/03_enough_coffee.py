water = int(input('Write how many ml of water the coffee machine has: '))
milk = int(input('Write how many ml of milk the coffee machine has: '))
beans = int(input('Write how many g of coffee beans the coffee machine has: '))
cups = int(input('Write how many cups of coffee you will need: '))

water_req = water // 200
milk_req = milk // 50 
beans_req = beans // 15
n = min(water_req, milk_req, beans_req)

if n == cups:
    print('Yes, I can make that amount of coffee')
elif n < cups:
    print('No, I can make only %s cups of coffee', str(n))
elif n > cups:
    print('Yes, I can make that amount of coffee (and even  ' + str(n - 1) + ' more than that)')
