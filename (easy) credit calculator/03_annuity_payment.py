import math


# calculate nominal interest
def calc_i(interest):
    i = (interest / 100) / 12
    return i


# calculate count of periods
def calc_n(p, a, i):
    n = math.log(a / (a - i * p), 1 + i)
    return math.ceil(n)


# calculate annuity payment
def calc_a(p, n, i):
    a = p * ((i * math.pow(1 + i, n)) / (pow(1 + i, n) - 1))
    return math.ceil(a)


# calculate credit principal
def calc_p(a, n, i):
    p = a / (i * math.pow(1 + i, n) / (math.pow(1 + i, n) - 1))
    return math.ceil(p)


calc = input("""What do you want to calculate?
        type 'n' - for count of months,
        type 'a' - for annuity monthly payment,
        type 'p' - for credit principal: """)
if calc == 'n':
    in_p = float(input('Enter credit principal: '))
    in_a = float(input('Enter monthly payment: '))
    in_int = float(input('Enter credit interest: '))
    n = calc_n(in_p, in_a, calc_i(in_int))
    years = math.floor(n / 12)
    months = n % 12
    if years > 1 and months != 0:
        print('You need ' + str(years) + ' years and ' + str(months) + ' months to repay this credit!')
    elif months == 0:
        print('You need ' + str(years) + ' years to repay this credit!')
    elif months < 13 and months > 1:
       print('You need ' + str(n) + ' months to repay this credit!')
    elif months == 1:
        print('You need ' + str(n) + ' month to repay this credit!')
elif calc == 'a':
    in_p = float(input('Enter credit principal: '))
    in_n = float(input('Enter count of periods: '))
    in_int = float(input('Enter credit interest: '))
    a = calc_a(in_p, in_n, calc_i(in_int))
    print('Your annuity payment = ' + str(a) + '!')
elif calc == 'p':
    in_a = float(input('Enter monthly payment: '))
    in_n = float(input('Enter count of periods: '))
    in_int = float(input('Enter credit interest: '))
    p = calc_p(in_a, in_n, calc_i(in_int))
    print('Your credit principal = ' + str(p) + '!')
