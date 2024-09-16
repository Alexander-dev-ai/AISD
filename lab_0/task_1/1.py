a, b = map(int, input().split())
while not(-10**9 <= a <= 10**9) or not(-10**9 <= b <= 10**9):
    print('error')
    a, b = map(int, input().split())
print(a + b)