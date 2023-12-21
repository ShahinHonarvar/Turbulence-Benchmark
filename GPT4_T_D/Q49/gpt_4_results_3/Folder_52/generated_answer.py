
def if_decimal_is_divisible(binary_string):
    fib_sequence = [0, 1]
    for _ in range(174):
        next_fib_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib_number)
    
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_sequence[176] == 0
