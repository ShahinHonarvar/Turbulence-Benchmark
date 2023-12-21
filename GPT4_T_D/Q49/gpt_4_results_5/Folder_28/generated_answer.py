
def if_decimal_is_divisible(binary_string):
    binary_to_decimal = int(binary_string, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 104:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    if binary_to_decimal % fib_sequence[103] == 0:
        return True
    else:
        return False
