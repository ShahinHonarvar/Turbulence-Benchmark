
def if_decimal_is_divisible(binary):
    a, b = 0, 1
    for _ in range(114):
        a, b = b, a + b
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * 2**(len(binary) - i - 1)
    return decimal % b == 0
