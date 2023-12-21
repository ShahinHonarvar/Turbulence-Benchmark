
def if_decimal_is_divisible(binary_str):
    i = 0
    decimal = 0
    for digit in binary_str[::-1]:
        decimal += int(digit) * (2 ** i)
        i += 1
        
    a, b = 0, 1
    for _ in range(170):
        a, b = b, a + b

    return decimal % b == 0
