
def if_decimal_is_divisible(binary_decimal):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal = int(binary_decimal, 2)
    fibonacci_178 = fibonacci(178)

    if decimal % fibonacci_178 == 0:
        return True
    else:
        return False
