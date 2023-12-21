
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    while len(fibonacci) < 177:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal = 0
    for i, bit in enumerate(binary):
        decimal += int(bit) * 2 ** (len(binary) - i - 1)
    return decimal % fibonacci[176] == 0
