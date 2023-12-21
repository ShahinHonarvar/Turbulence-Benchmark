
def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibonacci_sequence = [0, 1]
    i = 2
    while i < 74:
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
        i += 1
    return decimal % fibonacci_sequence[-1] == 0
