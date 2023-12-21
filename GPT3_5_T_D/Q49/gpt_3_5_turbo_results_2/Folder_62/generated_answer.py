
def if_decimal_is_divisible(dec):
    fib = [0, 1]
    while len(fib) < 130:
        fib.append(fib[-1] + fib[-2])
    
    decimal = int(dec, 2)
    
    if decimal % fib[129] == 0:
        return True
    else:
        return False
