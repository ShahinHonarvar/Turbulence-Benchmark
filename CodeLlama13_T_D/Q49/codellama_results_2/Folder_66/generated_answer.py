
def if_decimal_is_divisible(binary_representation):
    fibonacci = [0, 1]
    while True:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
        if len(fibonacci) == 120:
            break
    decimal = int(binary_representation, 2)
    return decimal % fibonacci[120] == 0
