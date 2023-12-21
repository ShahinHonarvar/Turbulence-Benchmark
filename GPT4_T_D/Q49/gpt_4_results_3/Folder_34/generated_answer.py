
def if_decimal_is_divisible(binary_string):
    num = int(binary_string, 2)
    fib_a, fib_b = 0, 1
    for _ in range(24):
        fib_a, fib_b = fib_b, fib_a + fib_b
    return num % fib_a == 0
