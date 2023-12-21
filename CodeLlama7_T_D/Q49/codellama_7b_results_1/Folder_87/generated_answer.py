
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Initialize the Fibonacci sequence with the first two numbers
    fibonacci_sequence = [0, 1]
    # Compute the 180th number in the Fibonacci sequence
    for i in range(180):
        fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-1])
    # Check if the decimal integer is divisible by the 180th number in the Fibonacci sequence
    return decimal_integer % fibonacci_sequence[180] == 0
