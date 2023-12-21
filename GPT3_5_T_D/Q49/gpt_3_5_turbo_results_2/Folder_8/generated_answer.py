
def if_decimal_is_divisible(decimal_str):
    fibonacci = [0, 1]
    while len(fibonacci) < 54:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    decimal = int(decimal_str, 2)
    
    return decimal % fibonacci[53] == 0
