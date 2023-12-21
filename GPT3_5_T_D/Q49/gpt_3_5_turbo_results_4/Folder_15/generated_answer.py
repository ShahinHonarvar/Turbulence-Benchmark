 
def if_decimal_is_divisible(binary_representation):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 9:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
      
    decimal_integer = int(binary_representation, 2)
    fibonacci_number = fibonacci_sequence[8]
    
    return decimal_integer % fibonacci_number == 0
