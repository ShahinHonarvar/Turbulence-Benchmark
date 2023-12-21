
def if_decimal_is_divisible(binary):
    a, b = 0, 1
    for _ in range(40):
        a, b = b, a + b
    decimal = int(binary, 2)
    return decimal % b == 0
