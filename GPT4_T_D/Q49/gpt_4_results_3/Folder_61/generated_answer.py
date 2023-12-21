
def if_decimal_is_divisible(binary_string):
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal = int(binary_string, 2)
    fib_76 = fib(76)
    return decimal % fib_76 == 0
