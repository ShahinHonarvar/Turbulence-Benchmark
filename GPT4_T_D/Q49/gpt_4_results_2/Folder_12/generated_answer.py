
def if_decimal_is_divisible(binary_representation):
    n = int(binary_representation, 2)
    a, b = 0, 1
    idx = 1
    while idx < 66:
        a, b = b, a + b
        idx += 1
    return n % b == 0
