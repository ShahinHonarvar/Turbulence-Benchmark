
def if_decimal_is_divisible(bin_string):
    fibonacci_sequence = [0, 1]
    
    while len(fibonacci_sequence) < 14:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        
    decimal_number = int(bin_string, 2)
    
    if decimal_number % fibonacci_sequence[13] == 0:
        return True
    else:
        return False
