
def if_decimal_is_divisible(binary_representation):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    fib_56th = fibonacci(56)
    decimal_integer = int(binary_representation, 2)

    if decimal_integer % fib_56th == 0:
        return True
    else:
        return False
