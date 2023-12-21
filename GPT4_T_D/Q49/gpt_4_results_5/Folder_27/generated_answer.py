
def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1]
    decimal_number = int(binary_string, 2)
    
    while len(fibonacci_sequence) < 87:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

    return decimal_number % fibonacci_sequence[-1] == 0
