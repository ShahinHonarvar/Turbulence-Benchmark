
def if_decimal_is_divisible(binary_representation):
    fibonacci = [0, 1]
    while len(fibonacci) < 187:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal = int(binary_representation, 2)
    return decimal % fibonacci[186] == 0
