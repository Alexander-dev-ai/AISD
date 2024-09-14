import time

start_time = time.time()

with open('input.txt') as f:
    n = f.readline()
n = int(n)


def calc_fib(n):
    if n <= 1:
        return n
    else:
        return calc_fib(n - 1) + calc_fib(n - 2)


if n < 0 or n > 45:
    print('Error')
else:
    fn = calc_fib(n)
    with open('output.txt', 'w') as f1:
        f1.write(str(fn))

end_time = time.time()
print('Время выполнения:', end_time - start_time)