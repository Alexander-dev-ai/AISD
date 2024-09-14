with open('input.txt') as f:
    a = f.readline()
    b = f.readline()

if (-10**9 <= int(a) <= 10**9) and (-10**9 <= int(b) <= 10**9):
    with open('output.txt', 'w') as f1:
        f1.write(str(int(a) + int(b)))
else:
    print('Error')