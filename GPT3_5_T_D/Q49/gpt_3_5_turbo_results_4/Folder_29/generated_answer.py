
def if_decimal_is_divisible(binary_repr):
    fib = [0, 1]
    for i in range(2, 118):
        fib.append(fib[i-1] + fib[i-2])
        
    decimal = int(binary_repr, 2)
    return decimal % fib[116] == 0
