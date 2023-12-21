
def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_sequence = [0, 1]
    while len(fib_sequence) < 126:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return decimal_number % fib_sequence[-1] == 0
