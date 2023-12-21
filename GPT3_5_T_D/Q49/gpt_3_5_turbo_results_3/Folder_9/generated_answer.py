
def if_decimal_is_divisible(decimal_str):
    fibonacci = [0, 1]
    
    while len(fibonacci) < 69:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    decimal_int = int(decimal_str, 2)
    return decimal_int % fibonacci[68] == 0
