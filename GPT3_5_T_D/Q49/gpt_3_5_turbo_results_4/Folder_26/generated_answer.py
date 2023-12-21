
def if_decimal_is_divisible(binary):
    fib_sequence = [0, 1]
    while len(fib_sequence) <= 138:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    
    decimal = int(binary, 2)
    
    if decimal % fib_sequence[137] == 0:
        return True
    else:
        return False
