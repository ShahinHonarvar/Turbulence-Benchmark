
def if_decimal_is_divisible(bin_string):
    fib_sequence = [0, 1]
    while len(fib_sequence) < 190:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    fib_number = fib_sequence[189]

    decimal_number = int(bin_string, 2)
    return decimal_number % fib_number == 0
