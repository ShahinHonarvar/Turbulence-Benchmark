
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Initialize a list to store the Fibonacci sequence numbers
    fibonacci_sequence = []
    # Generate the first two numbers of the Fibonacci sequence
    fibonacci_sequence.append(0)
    fibonacci_sequence.append(1)
    # Loop through the rest of the Fibonacci sequence numbers
    for i in range(2, len(fibonacci_sequence)):
        # Calculate the next number of the Fibonacci sequence using the previous two numbers
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    # Check if the decimal integer is divisible by the 78th number of the Fibonacci sequence
    if decimal_integer % fibonacci_sequence[77] == 0:
        return True

    else:

        return False
