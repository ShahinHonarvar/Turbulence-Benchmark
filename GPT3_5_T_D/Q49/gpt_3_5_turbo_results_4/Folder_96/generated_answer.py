

def if_decimal_is_divisible(s):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 48:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    
    decimal_number = int(s, 2)
    forty_seventh_fibonacci_number = fibonacci_sequence[46]
    
    return decimal_number % forty_seventh_fibonacci_number == 0
