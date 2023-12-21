
def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    x1, x2 = 0, 1
    for _ in range(45):
        x1, x2 = x2, x1 + x2
    return decimal % x1 == 0
