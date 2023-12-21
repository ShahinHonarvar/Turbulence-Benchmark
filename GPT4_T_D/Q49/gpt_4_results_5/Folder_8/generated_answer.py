
def if_decimal_is_divisible(binary_rep):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal = int(binary_rep, 2)
    fib_54 = fibonacci(54)

    return decimal % fib_54 == 0
