
def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, 2)

    fibonacci_sequence = [0, 1]
    for i in range(2, 97):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

    if decimal_integer % fibonacci_sequence[96] == 0:
        return True
    else:
        return False
