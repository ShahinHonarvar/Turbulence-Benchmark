
def if_decimal_is_divisible(bin_repr):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    decimal = int(bin_repr, 2)
    return decimal % fibonacci(68) == 0
