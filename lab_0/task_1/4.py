with open('input.txt') as f:
    a = f.readline()
    b = f.readline()

with open('output.txt', 'w') as f1:
    if (-10**9 <= int(a) <= 10**9) and (-10**9 <= int(b) <= 10**9):
        f1.write(str(int(a) + int(b)**2))
    else:
        f1.write('Error')