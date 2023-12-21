
def if_decimal_is_divisible(binary_string):
    num = int(binary_string, 2)
    a, b = 0, 1
    fib = 0
    for _ in range(35):
        fib = a + b
        a, b = b, fib
    return num % fib == 0
