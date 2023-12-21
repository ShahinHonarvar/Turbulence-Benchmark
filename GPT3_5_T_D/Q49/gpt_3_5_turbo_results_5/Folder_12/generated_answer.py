
def if_decimal_is_divisible(s):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal = 0
    for i, digit in enumerate(s):
        decimal += int(digit) * (2 ** (len(s)-1-i))

    fib_66 = fibonacci(66)
    return decimal % fib_66 == 0
