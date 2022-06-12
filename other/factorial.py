
def factorial(n):
    val= 1
    for i in range(n + 1):
        if i != 0:
            val *= i
    return val


def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


if __name__ == '__main__':
    print(factorial(5))
    print(factorial_recursive(5))
