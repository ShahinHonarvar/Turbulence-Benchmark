
def if_decimal_is_divisible(binary_str):
    def fibonacci(n):
        if n < 2: return n
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    fib_69 = fibonacci(69)
    dec_integer = int(binary_str, 2)
    if dec_integer % fib_69 == 0: return True
    return False
