
def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1]
    i = 2

    while len(fibonacci_sequence) < 28:
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
        i += 1

    decimal_number = int(binary_string, 2)

    if decimal_number % fibonacci_sequence[-1] == 0:
        return True
    else:
        return False
