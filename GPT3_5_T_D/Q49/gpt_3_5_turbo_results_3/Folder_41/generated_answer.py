
def if_decimal_is_divisible(decimal_binary):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 67:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    decimal_integer = int(decimal_binary, 2)
    return decimal_integer % fibonacci_sequence[66] == 0
