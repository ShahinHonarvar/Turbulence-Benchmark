
def if_decimal_is_divisible(bin_string):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) <= 138:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    target_number = fibonacci_sequence[138]

    decimal_number = int(bin_string, 2)
    return decimal_number % target_number == 0
