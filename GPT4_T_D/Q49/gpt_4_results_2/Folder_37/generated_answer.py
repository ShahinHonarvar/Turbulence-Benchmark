
def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1]
    for i in range(2, 46):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    
    decimal_number = int(binary_string, 2)
    
    return decimal_number % fibonacci_sequence[45] == 0
