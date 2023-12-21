
def if_decimal_is_divisible(binary_num):
    dec_num = int(binary_num, 2)
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 69:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return dec_num % fibonacci_sequence[68] == 0
