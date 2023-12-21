
def if_decimal_is_divisible(binary_representation):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < 110:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    
    decimal_number = int(binary_representation, 2)
    
    return decimal_number % fibonacci_sequence[110] == 0
