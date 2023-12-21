
def if_decimal_is_divisible(binary_repr):
    fib = [0, 1]
    for i in range(2, 69):
        fib.append(fib[i-2] + fib[i-1])
    
    decimal = int(binary_repr, 2)
    return decimal % fib[68] == 0
