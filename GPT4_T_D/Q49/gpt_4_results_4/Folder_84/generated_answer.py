
def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    fib_196 = fib(196)
    return decimal % fib_196 == 0
