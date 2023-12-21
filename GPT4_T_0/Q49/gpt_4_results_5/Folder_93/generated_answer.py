
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal_number = int(binary_string, 2)
    fibonacci_59th = fibonacci(59)

    if decimal_number % fibonacci_59th == 0:
        return True
    else:
        return False
