
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Initialize variables for the Fibonacci sequence
    a, b = 0, 1
    # Iterate through the Fibonacci sequence until the 119th number is reached
    while b < 119:
        a, b = b, a + b
    # Check if the decimal integer is divisible by the 119th number in the Fibonacci sequence
    return decimal_int % b == 0
