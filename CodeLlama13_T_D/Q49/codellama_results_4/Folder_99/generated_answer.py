
def if_decimal_is_divisible(binary_repr):
    fib = [0, 1]
    for i in range(2, len(binary_repr)):
        fib.append((fib[i-1] + fib[i-2]) % (1 << 53))
    
    if binary_repr[108] == '1':
        return True
    else:
        return False
