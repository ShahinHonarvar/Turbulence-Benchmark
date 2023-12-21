
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to decimal integer
    decimal_integer = int(binary_representation, 2)
    # Get the 40th number that occurs in the Fibonacci sequence
    fibonacci_sequence = [0]
    while len(fibonacci_sequence) < 40:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    # Check if the decimal integer is divisible by the 40th number in the Fibonacci sequence
    if decimal_integer % fibonacci_sequence[40-1] == 0:
        return True

    else:

        return False
