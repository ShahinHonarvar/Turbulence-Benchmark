
def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 59:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    number = int(binary_string, 2)
    return number % fibonacci_sequence[-1] == 0
