
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Initialize the Fibonacci sequence with the first two numbers
    fibonacci_seq = [0, 1]
    # Loop through the Fibonacci sequence until we find the 109th number
    for i in range(108):
        # Add the next two numbers in the Fibonacci sequence
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    # Check if the decimal integer is divisible by the 109th number in the Fibonacci sequence
    return decimal_int % fibonacci_seq[108] == 0
