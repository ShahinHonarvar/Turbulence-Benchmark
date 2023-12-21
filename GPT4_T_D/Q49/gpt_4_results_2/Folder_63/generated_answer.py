
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    dec_int = int(binary_str, 2)
    if dec_int % fibonacci(144) == 0:
        return True
    else:
        return False
