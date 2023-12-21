
def if_decimal_is_divisible(binary_string):
    binary_to_decimal = int(binary_string, 2)

    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 127:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        
    if binary_to_decimal % fibonacci_sequence[126] == 0:
        return True
    else:
        return False
