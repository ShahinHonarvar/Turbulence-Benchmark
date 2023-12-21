
def if_decimal_is_divisible(binary_str):
    num = int(binary_str, 2)
    f1, f2 = 0, 1
    for _ in range(128):
        f1, f2 = f2, f1 + f2
    return num % f2 == 0
