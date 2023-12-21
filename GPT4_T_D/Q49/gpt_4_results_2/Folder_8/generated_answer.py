
def if_decimal_is_divisible(bin_string):
    int_number = int(bin_string, 2)
    
    fib_sequence = [0, 1]
    i = 2
    while len(fib_sequence) <= 54:
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        i += 1
        
    return int_number % fib_sequence[53] == 0
