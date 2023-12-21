
def if_decimal_is_divisible(binary_representation):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal = int(binary_representation, 2)
    fibonacci_174 = fibonacci(174)

    if decimal % fibonacci_174 == 0:
        return True
    else:
        return False
