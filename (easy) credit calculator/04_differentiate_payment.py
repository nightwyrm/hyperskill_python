import math, argparse, sys


# calculate nominal interest
def calc_i(interest):
    i = (interest / 100) / 12
    return i


# calculate count of periods
def calc_n(P, A, i):
    n = math.log(A / (A - i * P), 1 + i)
    return math.ceil(n)


# calculate annuity payment
def calc_a(P, n, i):
    A = P * ((i * math.pow(1 + i, n)) / (pow(1 + i, n) - 1))
    return math.ceil(A)


# calculate credit principal
def calc_p(A, n, i):
    P = A / (i * math.pow(1 + i, n) / (math.pow(1 + i, n) - 1))
    return math.floor(P)


# calculate differentiated payment
def calc_d(P, i, n, m):
    D = (P / n) + i * (P - ((P * (m - 1)) / n))
    return math.ceil(D)


# construct the argument parser
def init_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('--type', help='the type of calculation required')
    ap.add_argument('--principal', type=float, help='the credit principal amount')
    ap.add_argument('--periods', type=int, help='the number of months')
    ap.add_argument('--payment', type=float, help='the annuity monthly payment amount')
    ap.add_argument('--interest', type=float, help='the credit interest rate')
    return ap


# main code
parser = init_args()
args = parser.parse_args()
if args.type not in ['diff', 'annuity']:
    print('Incorrect parameters.')
elif args.type == 'diff' and args.payment:
    print('Incorrect parameters.')
elif not args.interest:
    print('Incorrect parameters.')
elif len(sys.argv) < 4:
    print('Incorrect parameters.')
elif args.type == 'diff':
    total = 0
    for month in range(1, args.periods + 1):
        D = calc_d(args.principal, calc_i(args.interest), args.periods, month)
        print('Month ' + str(month) + ': paid out ' + str(D))
        total += D
        month += 1
    print('\nOverpayment = ' + str(total - math.ceil(args.principal)))
elif args.type == 'annuity':
    if not args.periods:
        n = calc_n(args.principal, args.payment, calc_i(args.interest))
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
        over = (math.ceil(args.payment) * n) - args.principal
        print('Overpayment = ' + str(over))
    elif not args.payment:
        A = calc_a(args.principal, args.periods, calc_i(args.interest))
        print('Your annuity payment = ' + str(A) + '!')
        over = (math.ceil(A) * args.periods) - args.principal
        print('Overpayment = ' + str(over))
    elif not args.principal:
        P = calc_p(args.payment, args.periods, calc_i(args.interest))
        print('Your credit principal = ' + str(P) + '!')
        over = (math.ceil(args.payment) * args.periods) - P
        print('Overpayment = ' + str(over))
