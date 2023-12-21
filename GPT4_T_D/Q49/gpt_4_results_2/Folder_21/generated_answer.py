
def if_decimal_is_divisible(bin_str):
    decimal = int(bin_str, 2)
    a, b = 0, 1
    fib_num = 0
    for _ in range(195):
        fib_num = a
        a, b = b, a + b
    return decimal % fib_num == 0
