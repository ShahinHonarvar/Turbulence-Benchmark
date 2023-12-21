
def if_decimal_is_divisible(binary_representation):
    fibonacci = [0, 1]
    while len(str(fibonacci[-1])) < len(binary_representation):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal_integer = int(binary_representation, 2)
    if len(fibonacci) >= 10 and decimal_integer % fibonacci[9] == 0:
        return True
    return False
