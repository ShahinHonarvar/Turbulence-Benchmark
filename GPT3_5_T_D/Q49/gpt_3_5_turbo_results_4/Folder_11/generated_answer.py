
def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    while fibonacci[-1] < 2**len(binary):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    decimal = int(binary, 2)
    if len(fibonacci) >= 16 and decimal % fibonacci[15] == 0:
        return True
    else:
        return False
