
def if_decimal_is_divisible(binary_string):
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return a

    decimal_integer = int(binary_string, 2)
    N = fib(85)
    return decimal_integer % N == 0
