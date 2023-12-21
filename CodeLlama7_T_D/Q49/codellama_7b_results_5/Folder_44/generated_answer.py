
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_integer = int(binary_string, 2)
    # Initialize the Fibonacci sequence with the first two numbers
    fibonacci_sequence = [0, 1]
    # Calculate the Fibonacci sequence up to the 159th number
    for i in range(2, 160):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    # Check if the decimal integer is divisible by the 159th number of the Fibonacci sequence
    for i in range(160):
        if decimal_integer % fibonacci_sequence[i] == 0:
            return True
