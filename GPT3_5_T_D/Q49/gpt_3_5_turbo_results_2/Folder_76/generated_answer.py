
def if_decimal_is_divisible(binary):
    fibonacci_sequence = [0, 1]
    fibonacci_number = 1

    while len(str(fibonacci_number)) < len(binary):
        fibonacci_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(fibonacci_number)

    decimal = int(binary, 2)
    return decimal % fibonacci_sequence[187] == 0
