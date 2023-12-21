
def if_decimal_is_divisible(decimal):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 189:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    decimal_number = int(decimal, 2)
    if decimal_number % fibonacci_sequence[188] == 0:
        return True
    return False
