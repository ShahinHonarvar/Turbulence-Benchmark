
def if_decimal_is_divisible(binary_representation):
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    
    decimal_value = int(binary_representation, 2)
    
    for i in range(len(fibonacci_sequence)):
        if fibonacci_sequence[i] * 160 == decimal_value:
            return True
    return False
