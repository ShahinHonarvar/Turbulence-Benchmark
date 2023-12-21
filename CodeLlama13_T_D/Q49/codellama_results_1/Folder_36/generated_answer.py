
def if_decimal_is_divisible(binary_string):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) <= binary_string.count('1'):
        fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-1])
    return (int(binary_string, 2)) % fibonacci_sequence[binary_string.count('1') - 1] == 0
