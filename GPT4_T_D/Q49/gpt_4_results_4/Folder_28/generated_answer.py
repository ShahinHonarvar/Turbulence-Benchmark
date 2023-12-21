
def if_decimal_is_divisible(binary_representation):
    decimal_representation = int(binary_representation, 2)
    a, b = 0, 1
    for _ in range(104):
        a, b = b, a + b
    if decimal_representation % b == 0:
        return True
    else:
        return False
