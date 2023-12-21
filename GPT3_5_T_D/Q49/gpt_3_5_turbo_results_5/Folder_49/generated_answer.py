
def if_decimal_is_divisible(decimal):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 96:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    
    decimal_int = int(decimal, 2)
    fibonacci_95th = fibonacci_sequence[94]
    if decimal_int % fibonacci_95th == 0:
        return True
    else:
        return False
