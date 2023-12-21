
def if_decimal_is_divisible(binary_str):
    num = int(binary_str, 2)
    a, b = 0, 1
    fib = 0
    for i in range(119):
        fib = a
        a, b = b, a + b
    return num % fib == 0
