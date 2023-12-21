
def if_decimal_is_divisible(binary):
    fibonacci = []
    fibonacci.append(0)
    fibonacci.append(1)
    
    while len(fibonacci) < 161:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    decimal = int(binary, 2)
    
    return decimal % fibonacci[160] == 0
