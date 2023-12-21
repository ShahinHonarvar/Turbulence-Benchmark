
def if_decimal_is_divisible(binary_dec):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    dec_int = int(binary_dec, 2)
    fibonacci_40th = fibonacci(40)

    return dec_int % fibonacci_40th == 0
