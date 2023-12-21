
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Initialize the Fibonacci sequence with the first two numbers
    fibonacci_sequence = [0, 1]
    # Iterate through the Fibonacci sequence until we find the 126th number
    for i in range(125):
        # Add the next two numbers in the Fibonacci sequence
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    # Check if the decimal integer is divisible by the 126th number in the Fibonacci sequence
    return decimal_integer % fibonacci_sequence[125] == 0
