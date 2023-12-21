
def if_decimal_is_divisible(decimal):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < 10**len(decimal):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return int(decimal, 2) % fibonacci_sequence[170] == 0
