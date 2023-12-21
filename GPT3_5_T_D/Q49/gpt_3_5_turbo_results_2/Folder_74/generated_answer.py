
def if_decimal_is_divisible(binary):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 166:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    decimal = int(binary, 2)
    return decimal % fibonacci_sequence[165] == 0
