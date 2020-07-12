import math

def pmt_amt(principal, months):
    amt = math.ceil(principal / months)
    return amt

def last_pmt(principal, months, pmt):
    amt = math.ceil(principal - (months - 1) * pmt)
    return amt

def rem_mnths(principal, pmt):
    rem = math.ceil(principal / pmt)
    return rem

print('Enter the credit principal:')
principal = int(input())
print("""What do you want to calculate?
        type 'm' - for count of months,
        type 'p' - for monthly payment:""")
calc_type = input()
if calc_type == 'm':
    print('Enter monthly payment:')
    payment = int(input())
    period = rem_mnths(principal, payment)
    if period > 1:
        print('\nIt takes ' + str(period) + ' months to repay the credit.')
    elif period == 1:
        print('\nIt takes ' + str(period) + ' month to repay the credit.')
elif calc_type == 'p':
    print('Enter count of months:')
    months = int(input())
    mth_payment = pmt_amt(principal, months)
    lst_payment = last_pmt(principal, months, mth_payment)
    if lst_payment < mth_payment:
        print('\nYour monthly payment = ' + str(mth_payment) + ' with last month payment = ' + str(lst_payment) + '.')
    else:
        print('\nYour monthly payment = ' + str(mth_payment) + '.')
