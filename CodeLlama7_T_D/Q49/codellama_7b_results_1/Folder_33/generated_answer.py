
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Initialize variables for Fibonacci sequence
    a, b = 0, 1
    # Calculate the 134th number in the Fibonacci sequence
    for _ in range(134):
        a, b = b, a + b
    # Check if the decimal integer is divisible by the 134th number in the Fibonacci sequence
    return decimal_int % b == 0
