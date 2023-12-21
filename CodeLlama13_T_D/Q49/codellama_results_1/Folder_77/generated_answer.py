
def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, len(fib)):
        fib.append(fib[i-2] + fib[i-1])
    
    decimal = int(binary_str, 2)
    return decimal % fib[110] == 0
