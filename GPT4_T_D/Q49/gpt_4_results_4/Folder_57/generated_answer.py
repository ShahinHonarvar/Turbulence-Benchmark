
def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1]
    decimal_integer = int(binary_string, 2)

    while len(fibonacci_sequence) < 80:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        
    if decimal_integer % fibonacci_sequence[79] == 0:
        return True
    else:
        return False
