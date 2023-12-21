
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to decimal integer
    decimal_integer = int(binary_representation, 2)
    # Get the Fibonacci sequence up to the 118th number
    fibonacci_sequence = [0, 1]
    for i in range(2, 119):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    # Check if the decimal integer is divisible by the 118th number of the Fibonacci sequence
    for i in range(2, 119):
        if decimal_integer % fibonacci_sequence[i] == 0:
            return True

    return False
