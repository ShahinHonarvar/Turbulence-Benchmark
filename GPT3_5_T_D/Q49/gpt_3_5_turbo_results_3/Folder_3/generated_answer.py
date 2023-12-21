
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    decimal_number = int(binary_string, 2)
    fibonacci_35th = fibonacci(35)

    return decimal_number % fibonacci_35th == 0
