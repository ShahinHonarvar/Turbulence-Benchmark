
def if_decimal_is_divisible(binary_str):
    n = int(binary_str, 2)
    a, b = 0, 1
    fib = 0
    for _ in range(176):
        fib = a
        a, b = b, a + b
    return n % fib == 0
