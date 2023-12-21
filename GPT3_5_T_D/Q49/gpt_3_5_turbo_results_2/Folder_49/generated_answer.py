
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    fib_95 = fibonacci(95)
    decimal_int = int(binary_string, 2)

    if decimal_int % fib_95 == 0:
        return True
    else:
        return False
