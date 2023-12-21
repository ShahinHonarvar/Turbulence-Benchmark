
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal = int(binary_str, 2)
    fib_78 = fibonacci(78)

    return decimal % fib_78 == 0
