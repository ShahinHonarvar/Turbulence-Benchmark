
def if_decimal_is_divisible(binary_str):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 15:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    
    decimal = int(binary_str, 2)
    
    return decimal % fibonacci_sequence[13] == 0
