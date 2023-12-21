
def if_decimal_is_divisible(binary_string):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    dec_int = int(binary_string, 2)
    return dec_int % fibonacci(14) == 0
