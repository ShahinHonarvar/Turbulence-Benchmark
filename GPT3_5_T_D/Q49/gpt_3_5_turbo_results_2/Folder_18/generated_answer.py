
def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    
    while len(fibonacci) < 199:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    decimal = int(binary_string, 2)
    
    return decimal % fibonacci[198] == 0
