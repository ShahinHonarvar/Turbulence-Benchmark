
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    fib_176 = list(fibonacci(177))[-1]
    decimal = int(binary_string, 2)
    return decimal % fib_176 == 0
