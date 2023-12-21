
def if_decimal_is_divisible(bin_string):
    decimal_num = int(bin_string, 2)

    a, b = 0, 1
    for _ in range(60):
        a, b = b, a + b

    return decimal_num % b == 0
