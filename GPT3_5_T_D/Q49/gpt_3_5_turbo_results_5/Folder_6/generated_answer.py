
def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    while len(fibonacci) < 185:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    decimal_int = int(binary_str, 2)
    
    return decimal_int % fibonacci[184] == 0
