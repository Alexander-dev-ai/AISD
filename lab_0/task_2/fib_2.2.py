import time

start_time = time.time()

with open('input.txt') as f:
    n = int(f.readline())

f0 = 0
f1 = 1
with open('output.txt', 'w') as f:
    if n < 0 or n > 45:
        f.write('Error')
    elif n == 1:
        f.write('0')
    elif n == 2:
        f.write('1')
    else:
        for i in range(n - 2):
            f0, f1 = f1, f1 + f0
        f.write(str(f1))

end_time = time.time()
print(f'Время выполнения кода: {end_time - start_time}')
