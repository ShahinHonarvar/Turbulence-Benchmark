
def if_decimal_is_divisible(decimal):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return (fibonacci(n - 1) + fibonacci(n - 2))

    fibonacci_60 = fibonacci(60)

    decimal_int = int(decimal, 2)
    if decimal_int % fibonacci_60 == 0:
        return True
    else:
        return False
