with open('input.txt') as f:
    n = int(f.readline())


f0 = 0
f1 = 1
if n < 0 or n > 45:
    print('Error')
else:
    for i in range(n - 2):
        f0, f1 = f1, f1 + f0
    with open('output.txt', 'w') as f:
        f.write(str(f1))