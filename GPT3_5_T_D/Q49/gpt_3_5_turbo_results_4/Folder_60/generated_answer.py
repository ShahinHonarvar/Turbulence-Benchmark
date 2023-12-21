
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            a, b = 0, 1
            for _ in range(n - 1):
                a, b = b, a + b
            return b

    decimal = int(binary_str, 2)
    fib_number = fibonacci(107)
    return decimal % fib_number == 0
