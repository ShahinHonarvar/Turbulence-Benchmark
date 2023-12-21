
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    dec_num = int(binary_str, 2)
    return dec_num % fibonacci(135) == 0
