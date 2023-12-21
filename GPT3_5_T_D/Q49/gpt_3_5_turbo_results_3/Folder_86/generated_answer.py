
def if_decimal_is_divisible(binary):
    fib = [0, 1] 
    while True:
        fib.append(fib[-1] + fib[-2])
        if len(fib) == 136:
            break
    decimal = int(binary, 2)
    return decimal % fib[135] == 0
