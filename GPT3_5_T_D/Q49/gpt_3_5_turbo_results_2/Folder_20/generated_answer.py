
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return (fibonacci(n-1) + fibonacci(n-2))

    fibonacci_100 = fibonacci(100)
    decimal_int = int(binary_str, 2)

    if decimal_int % fibonacci_100 == 0:
        return True
    else:
        return False
