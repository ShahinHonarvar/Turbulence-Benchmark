
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal_number = int(binary_string, 2)
    fibonacci_number = fibonacci(117)

    if decimal_number % fibonacci_number == 0:
        return True
    else:
        return False
