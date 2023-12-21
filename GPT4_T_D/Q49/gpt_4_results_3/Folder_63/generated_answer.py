
def if_decimal_is_divisible(bin_str):
    decimal_num = int(bin_str, 2)

    # Fibonacci sequence
    a, b = 0, 1
    for _ in range(144):
        a, b = b, a + b

    return decimal_num % a == 0
