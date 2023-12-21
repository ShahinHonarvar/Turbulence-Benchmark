
def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fibonacci_sequence = [0, 1]
    
    for i in range(2, 98):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
        
    if decimal_number % fibonacci_sequence[97] == 0:
        return True
    else:
        return False
