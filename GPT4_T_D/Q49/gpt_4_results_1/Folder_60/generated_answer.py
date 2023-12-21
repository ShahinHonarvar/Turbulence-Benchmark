
def if_decimal_is_divisible(binary_string):
    binary_number = int(binary_string, 2)
    a, b = 0, 1
    for _ in range(108):
        a, b = b, a + b
    return binary_number % a == 0
