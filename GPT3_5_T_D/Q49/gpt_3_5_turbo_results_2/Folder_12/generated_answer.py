
def if_decimal_is_divisible(binary_representation):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < 10**len(binary_representation):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    decimal_integer = int(binary_representation, 2)
    return decimal_integer % fib_sequence[65] == 0
