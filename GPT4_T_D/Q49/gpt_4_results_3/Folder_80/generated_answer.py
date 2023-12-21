
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    decimal_integer = int(binary_string, 2)
    fibonacci_179 = fibonacci(179)
    return decimal_integer % fibonacci_179 == 0
