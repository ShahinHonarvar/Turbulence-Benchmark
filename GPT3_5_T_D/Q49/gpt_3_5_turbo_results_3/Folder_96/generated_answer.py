
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_1 = 0
        fib_2 = 1
        for i in range(2, n+1):
            fib_current = fib_1 + fib_2
            fib_1 = fib_2
            fib_2 = fib_current
        return fib_2

def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib_47 = fibonacci(47)
    return decimal % fib_47 == 0
