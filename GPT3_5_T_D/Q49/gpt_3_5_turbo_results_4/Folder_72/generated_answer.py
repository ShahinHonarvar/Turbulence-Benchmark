
def if_decimal_is_divisible(binary):
    fib = [0, 1]
    while len(fib) < 176:
        fib.append(fib[-1] + fib[-2])
    
    decimal = int(binary, 2)
    if decimal % fib[175] == 0:
        return True
    else:
        return False
