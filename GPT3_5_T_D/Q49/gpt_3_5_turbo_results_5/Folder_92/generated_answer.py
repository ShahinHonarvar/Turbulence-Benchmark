
def if_decimal_is_divisible(binary_str):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 7:
        next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_num)
    decimal_integer = int(binary_str, 2)
    return decimal_integer % fibonacci_sequence[6] == 0
