
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(n - 1):
                a, b = b, a + b
            return b

    decimal_int = int(binary_str, 2)
    fibonacci_147 = fibonacci(147)
    return decimal_int % fibonacci_147 == 0
