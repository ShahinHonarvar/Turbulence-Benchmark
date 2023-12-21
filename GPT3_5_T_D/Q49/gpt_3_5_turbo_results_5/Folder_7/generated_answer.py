
def if_decimal_is_divisible(binary_str):
    fibonacci_sequence = [0, 1]
    for i in range(2, 161):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    
    decimal_number = int(binary_str, 2)
    
    if decimal_number % fibonacci_sequence[160] == 0:
        return True
    else:
        return False
