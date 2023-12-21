
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_num_sequence = [0, 1]
    while len(fib_num_sequence) < 50:
        fib_num_sequence.append(fib_num_sequence[-1] + fib_num_sequence[-2])
    if decimal % fib_num_sequence[49] == 0:
        return True
    else:
        return False
