
def if_decimal_is_divisible(binary_representation):
    fib_seq = [0, 1]
    for i in range(2, 136):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    
    decimal_integer = 0
    for i, bit in enumerate(binary_representation[::-1]):
        if bit == '1':
            decimal_integer += fib_seq[i]
    
    return decimal_integer % fib_seq[135] == 0
