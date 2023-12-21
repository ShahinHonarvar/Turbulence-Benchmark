
def if_decimal_is_divisible(bin_string):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal = int(bin_string, 2)
    fib27 = fibonacci(27)
    return decimal % fib27 == 0
