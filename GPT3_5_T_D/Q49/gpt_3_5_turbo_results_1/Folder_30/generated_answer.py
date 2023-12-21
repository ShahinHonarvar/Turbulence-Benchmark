
def if_decimal_is_divisible(binary_number):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal_number = int(binary_number, 2)
    fibonacci_number = fibonacci(186)

    if decimal_number % fibonacci_number == 0:
        return True
    else:
        return False
