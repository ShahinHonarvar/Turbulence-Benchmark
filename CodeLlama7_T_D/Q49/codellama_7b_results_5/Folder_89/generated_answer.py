
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Find the first occurrence of the 126th Fibonacci number in the sequence
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 126:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    # Check if the decimal integer is divisible by the corresponding Fibonacci number
    for i in range(len(fibonacci_sequence)):
        if decimal_integer % fibonacci_sequence[i] == 0:
            return True

    return False
