
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal = int(binary_str, 2)
    fib_94 = fibonacci(94)

    return decimal % fib_94 == 0
