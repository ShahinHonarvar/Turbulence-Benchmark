
def if_decimal_is_divisible(binary):
    fib = [0, 1]
    while len(fib) < 60:
        fib.append(fib[-1] + fib[-2])
    
    decimal = 0
    for digit in binary:
        decimal = (decimal << 1) | int(digit)
    
    return decimal % fib[58] == 0
