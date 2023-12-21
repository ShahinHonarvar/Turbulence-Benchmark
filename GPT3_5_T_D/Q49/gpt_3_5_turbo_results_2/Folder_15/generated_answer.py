
def if_decimal_is_divisible(binary):
    fibonacci_sequence = [0, 1]
    while len(str(fibonacci_sequence[-1])) < len(binary):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    decimal = int(binary, 2)
    if len(fibonacci_sequence) >= 9 and decimal % fibonacci_sequence[8] == 0:
        return True
    else:
        return False
