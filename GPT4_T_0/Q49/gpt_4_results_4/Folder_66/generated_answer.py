
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal_number = int(binary_string, 2)
    fibonacci_120th = fibonacci(120)

    return decimal_number % fibonacci_120th == 0
