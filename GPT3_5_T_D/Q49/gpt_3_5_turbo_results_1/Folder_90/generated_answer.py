
def if_decimal_is_divisible(decimal):
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    fibonacci_177 = fibonacci(177)
    decimal_int = int(decimal, 2)
    return decimal_int % fibonacci_177 == 0
