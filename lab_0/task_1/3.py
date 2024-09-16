with open('input.txt') as f:
    a, b = map(int, f.readline().split())

with open('output.txt', 'w') as f1:
    if (-10**9 <= int(a) <= 10**9) or (-10**9 <= int(b) <= 10**9):
        f1.write(str(int(a) + int(b)))
    else:
        f1.write('Error')