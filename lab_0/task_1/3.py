with open('input.txt') as f:
    a = f.readline()
    b = f.readline()

with open('output.txt', 'w') as f1:
    f1.write(str(int(a) + int(b)))