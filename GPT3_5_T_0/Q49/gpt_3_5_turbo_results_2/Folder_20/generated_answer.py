
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal = int(binary, 2)
    fibonacci_100 = fibonacci(100)

    if decimal % fibonacci_100 == 0:
        return True
    else:
        return False
