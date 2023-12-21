
def if_decimal_is_divisible(binary):
    fib = [0, 1]
    while len(fib) < 195:
        fib.append(fib[-1] + fib[-2])
    
    decimal = 0
    for i, b in enumerate(binary[::-1]):
        decimal += int(b) * (2 ** i)
    
    return decimal % fib[194] == 0
