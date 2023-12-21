
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    decimal_int = int(binary_string, 2)

    fib_num = list(fibonacci(29))[-1]

    return decimal_int % fib_num == 0
