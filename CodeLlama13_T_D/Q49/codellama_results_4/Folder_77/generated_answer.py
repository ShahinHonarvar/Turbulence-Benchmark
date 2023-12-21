
def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fibonacci = [0, 1]
    while len(fibonacci) <= decimal:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    return True if decimal % fibonacci[110] == 0 else False
