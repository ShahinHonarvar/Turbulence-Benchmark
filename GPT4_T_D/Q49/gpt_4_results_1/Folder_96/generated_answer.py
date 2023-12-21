
def if_decimal_is_divisible(binary_representation):
    fibonacci_sequence = [0, 1]
    for _ in range(45):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    
    decimal = int(binary_representation, 2)

    return decimal % fibonacci_sequence[47] == 0
