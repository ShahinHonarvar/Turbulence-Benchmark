
def if_decimal_is_divisible(binary_representation):
    a = 0
    b = 1
    for _ in range(33):
        a, b = b, a + b
    decimal_integer = int(binary_representation, 2)
    return decimal_integer % b == 0
