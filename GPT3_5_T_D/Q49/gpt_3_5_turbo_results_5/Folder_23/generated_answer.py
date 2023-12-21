
def if_decimal_is_divisible(binary_representation):
    fibonacci = [0, 1]
    while len(fibonacci) < 49:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    decimal = 0
    power = len(binary_representation) - 1
    for digit in binary_representation:
        decimal += int(digit) * (2 ** power)
        power -= 1
    
    return decimal % fibonacci[48] == 0
