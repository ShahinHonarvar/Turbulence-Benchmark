
def if_decimal_is_divisible(binary_decimal):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 86:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    
    decimal_integer = int(binary_decimal, 2)
    return decimal_integer % fibonacci_sequence[85] == 0
