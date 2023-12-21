
def if_decimal_is_divisible(binary_representation):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    fibonacci_110 = fibonacci(110)
    decimal_integer = int(binary_representation, 2)

    if decimal_integer % fibonacci_110 == 0:
        return True
    else:
        return False
