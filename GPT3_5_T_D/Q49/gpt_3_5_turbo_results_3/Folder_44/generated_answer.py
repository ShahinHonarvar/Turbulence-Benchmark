
def if_decimal_is_divisible(binary):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 160:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    decimal = int(binary, 2)
    return decimal % fib_sequence[159] == 0
