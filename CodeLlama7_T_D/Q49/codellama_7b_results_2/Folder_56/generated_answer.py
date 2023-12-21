
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_integer = int(binary_string, 2)
    # Initialize variables for the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    # Calculate the Fibonacci sequence until we reach the 84th number
    while len(fibonacci_sequence) < 85:
        fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-1])
    # Check if the decimal integer is divisible by the 84th Fibonacci number
    return (decimal_integer % fibonacci_sequence[83]) == 0
