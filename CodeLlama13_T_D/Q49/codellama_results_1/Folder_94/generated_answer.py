
def if_decimal_is_divisible(binary):
    fib = [0, 1]
    for i in range(2, 40):
        fib.append(fib[i-1] + fib[i-2])
    
    num = int(binary, 2)
    
    return num % fib[39] == 0
