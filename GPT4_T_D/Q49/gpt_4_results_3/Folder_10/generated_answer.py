
def if_decimal_is_divisible(bin_str):
    decimal = int(bin_str, 2)
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 88:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return decimal % fibonacci_sequence[-1] == 0
