while True:
    cmd = input().strip()
    if cmd == '/exit':
        print('Bye!')
        exit()
    elif cmd == '/help':
        print('The program calculates the sum of numbers')
    elif len(cmd) == 0:
        pass
    else:
        print(sum(int(n) for n in cmd.split()))
