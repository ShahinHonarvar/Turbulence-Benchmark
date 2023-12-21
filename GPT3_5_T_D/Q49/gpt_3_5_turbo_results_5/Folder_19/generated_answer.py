
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    while len(fibonacci) < 30:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)

    if decimal % fibonacci[28] == 0:
        return True
    else:
        return False
