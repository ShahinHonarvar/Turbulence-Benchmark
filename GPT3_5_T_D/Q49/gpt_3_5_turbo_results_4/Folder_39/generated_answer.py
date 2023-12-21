
def if_decimal_is_divisible(binary_repr):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal = int(binary_repr, 2)
    fibonacci_15 = fibonacci(14)

    if decimal % fibonacci_15 == 0:
        return True
    else:
        return False
