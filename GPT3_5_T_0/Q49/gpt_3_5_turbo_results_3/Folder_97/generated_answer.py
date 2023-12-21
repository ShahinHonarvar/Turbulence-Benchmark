
def if_decimal_is_divisible(binary):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal = int(binary, 2)
    fibonacci_114 = fibonacci(114)

    if decimal % fibonacci_114 == 0:
        return True
    else:
        return False
