
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Initialize variables for the Fibonacci sequence
    a = 0
    b = 1
    # Check if the decimal integer is divisible by the 128th number in the Fibonacci sequence
    while b < 128:
        a, b = b, a + b
    return decimal_integer % b == 0
