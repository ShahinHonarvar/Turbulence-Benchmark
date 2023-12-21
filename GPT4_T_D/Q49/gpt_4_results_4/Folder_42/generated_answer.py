
def if_decimal_is_divisible(binary_repr):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal = int(binary_repr, 2)
    divisor = fibonacci(146)
    return decimal % divisor == 0
