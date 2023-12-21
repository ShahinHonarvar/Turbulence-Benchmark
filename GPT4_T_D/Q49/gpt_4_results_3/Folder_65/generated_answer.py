
def if_decimal_is_divisible(bin_string):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    return int(bin_string, 2) % fibonacci(127) == 0
