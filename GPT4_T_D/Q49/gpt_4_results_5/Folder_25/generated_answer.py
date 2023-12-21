
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal_num = int(binary_str, 2)
    fibonacci_19 = fibonacci(19)

    return decimal_num % fibonacci_19 == 0
