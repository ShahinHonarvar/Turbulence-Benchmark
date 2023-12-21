
def if_decimal_is_divisible(bin_string):
    decimal = int(bin_string, 2)
    a, b = 0, 1
    for _ in range(90):
        a, b = b, a + b
    fib_90 = b
    return decimal % fib_90 == 0
