
def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1]
    for i in range(2, len(binary_string)):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    
    decimal_number = int(binary_string, 2)
    if decimal_number % fibonacci_sequence[18] == 0:
        return True
    else:
        return False
