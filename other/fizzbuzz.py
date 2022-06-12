
# 扱う数の上限
NUMS = 100
NUMS += 1

# fizzbuzz
for i in range(1, NUMS):
    print(f'{i}: ', end='')
    if i % 3 == 0:
        print('Fizz', end='')
    if i % 5 == 0:
        print('Buzz', end='')
    print()
