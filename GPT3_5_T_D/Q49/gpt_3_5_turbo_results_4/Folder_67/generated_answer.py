
def if_decimal_is_divisible(binary_string):
    fib_sequence = [0, 1]
    
    while len(str(fib_sequence[-1])) < len(binary_string):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    decimal_num = int(binary_string, 2)
    return decimal_num % fib_sequence[106] == 0
