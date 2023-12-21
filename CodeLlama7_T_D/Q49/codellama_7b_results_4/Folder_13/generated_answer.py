
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Initialize the Fibonacci sequence with the first two numbers
    fibonacci_sequence = [0, 1]
    # Iterate through the Fibonacci sequence until we reach the 174th number
    for i in range(173):
        # Add the last two numbers of the sequence to get the next number
        fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-1])
    # Check if the decimal integer is divisible by the 174th Fibonacci number
    return decimal_integer % fibonacci_sequence[173] == 0
