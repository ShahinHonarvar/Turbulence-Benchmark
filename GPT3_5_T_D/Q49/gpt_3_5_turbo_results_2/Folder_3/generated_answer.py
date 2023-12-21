
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    decimal_int = int(binary_str, 2)
    fibonacci_35th = fibonacci(35)

    if decimal_int % fibonacci_35th == 0:
        return True
    else:
        return False
