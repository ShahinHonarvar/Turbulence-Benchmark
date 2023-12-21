
def if_decimal_is_divisible(binary_representation):
    fib_sequence = [0, 1]
    while len(fib_sequence) <= 107:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    decimal = int(binary_representation, 2)
    return decimal % fib_sequence[107] == 0
