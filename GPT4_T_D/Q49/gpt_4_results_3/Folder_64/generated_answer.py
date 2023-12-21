
def if_decimal_is_divisible(binary_string):
    fib = [0, 1]
    while len(fib) < 10:
        fib.append(fib[-1] + fib[-2])
    
    decimal_int = int(binary_string, 2)
    
    if decimal_int % fib[9] == 0:
        return True
    else:
        return False
