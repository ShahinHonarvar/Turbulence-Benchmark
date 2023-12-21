
def if_decimal_is_divisible(binary_representation):
    fibonacci_sequence = [0, 1]
    for i in range(2, 16):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    decimal = int(binary_representation, 2)
    if decimal % fibonacci_sequence[15] == 0:
        return True
    else:
        return False
