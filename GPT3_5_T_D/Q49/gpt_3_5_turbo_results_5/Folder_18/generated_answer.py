
def if_decimal_is_divisible(binary_representation):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 199:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    
    decimal_integer = int(binary_representation, 2)
    return decimal_integer % fibonacci_sequence[198] == 0
