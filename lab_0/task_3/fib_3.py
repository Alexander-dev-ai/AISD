import time

start_time = time.time()

with open('input.txt') as f:
    n = int(f.readline())

f_1 = 1
f_2 = 1
with open('output.txt', 'w') as f:
    if n < 0 or n > 10 ** 7:
        print('Error')
    elif n == 0:
        f.write('0')
    elif n == 1 or n == 2:
        f.write('1')
    else:
        for i in range(n - 2):
            f_1, f_2 = f_2, f_1 + f_2
        f.write(str(f_2 % 10))

end_time = time.time()
print(f'Время выполнения кода: {end_time - start_time}')
