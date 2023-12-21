
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    a, b = 0, 1
    for i in range(29):
        a, b = b, a + b
    return decimal % a == 0
