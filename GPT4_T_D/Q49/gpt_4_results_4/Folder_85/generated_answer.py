
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_sequence = [0, 1]
    for i in range(2, 45):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    
    fib_45th = fib_sequence[-1]

    return decimal % fib_45th == 0
