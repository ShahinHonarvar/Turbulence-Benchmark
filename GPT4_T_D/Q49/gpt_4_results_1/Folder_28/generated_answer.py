
def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 104:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    
    decimal_number = int(binary_string, 2)
    if decimal_number % fibonacci_sequence[103] == 0:
        return True
    else:
        return False
