
def if_decimal_is_divisible(decimal):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 49:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    decimal_int = int(decimal, 2)
    return decimal_int % fibonacci_sequence[48] == 0
