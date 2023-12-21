
def if_decimal_is_divisible(binary_string):
    num_decimal = int(binary_string, 2)
    fib_sequence = [0, 1]
    
    while len(fib_sequence) < 160:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
     
    return num_decimal % fib_sequence[158] == 0
