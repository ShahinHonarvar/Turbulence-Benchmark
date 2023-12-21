
def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    while len(fibonacci) < 151:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    decimal = 0
    for digit in binary_string:
        decimal = decimal * 2 + int(digit)
    
    return decimal % fibonacci[149] == 0
