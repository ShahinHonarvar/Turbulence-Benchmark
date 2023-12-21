
def if_decimal_is_divisible(binary_rep):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal = int(binary_rep, 2)
    fib_74 = fibonacci(74)

    if decimal % fib_74 == 0:
        return True
    else:
        return False
