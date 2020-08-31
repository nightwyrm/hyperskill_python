from collections import deque


while True:
    cmd = input().strip()
    if cmd == '/exit':
        print('Bye!')
        exit()
    elif cmd == '/help':
        print('The program calculates stuff with numbers')
    elif len(cmd) == 0:
        pass
    else:
        values = deque()
        for x in cmd.split():
            values.append(x)
        total = int(values.popleft())
        while len(values) != 0:
            val = values.popleft()
            if '+' in val or '-' in val:
                if '+' in val or val.count('-') % 2 == 0:
                    total += int(values.popleft())
                elif '-' in val:
                    total -= int(values.popleft())
        print(total)
