
def if_decimal_is_divisible(binary_repr):
    fibonacci = [0, 1]
    for i in range(2, 118):
        fibonacci.append((fibonacci[i-1] + fibonacci[i-2]) % (1 << 32))
    
    dec = int(binary_repr, 2)
    return dec % fibonacci[117] == 0
