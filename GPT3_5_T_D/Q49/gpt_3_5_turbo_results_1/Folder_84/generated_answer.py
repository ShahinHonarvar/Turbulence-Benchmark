
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    while len(fibonacci) < 197:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal % fibonacci[196] == 0
