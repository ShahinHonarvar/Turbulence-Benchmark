
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    decimal_integer = int(binary_string, 2)
    fibonacci_76th = fibonacci(76)

    return decimal_integer % fibonacci_76th == 0
