
def if_decimal_is_divisible(binary_string):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 110:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    decimal_num = int(binary_string, 2)
    if decimal_num % fib_sequence[109] == 0:
        return True
    else:
        return False
