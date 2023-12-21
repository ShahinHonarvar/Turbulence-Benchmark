
def if_decimal_is_divisible(decimal):
    fibonacci = [0, 1]
    while len(fibonacci) < 89:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        
    decimal = int(decimal, 2)
    
    if decimal % fibonacci[88] == 0:
        return True
    else:
        return False
