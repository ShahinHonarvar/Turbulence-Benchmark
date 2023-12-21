
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        if n < 2:
            return n
        else:
            a, b = 0, 1
            for _ in range(n - 1):
                a, b = b, a + b
            return b

    decimal_integer = int(binary_string, 2)
    fib_127th = fibonacci(127)
    return decimal_integer % fib_127th == 0
