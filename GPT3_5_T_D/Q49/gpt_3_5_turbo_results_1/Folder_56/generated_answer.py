
def if_decimal_is_divisible(decimal):
    if decimal == '0':
        return True
    a, b = 0, 1
    for _ in range(84):
        a, b = b, a + b
    return int(decimal, 2) % a == 0
