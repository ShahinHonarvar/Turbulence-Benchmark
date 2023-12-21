
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Initialize variables for the Fibonacci sequence
    a, b = 0, 1
    # Check if the decimal integer is divisible by the 146th number in the Fibonacci sequence
    while a < decimal_integer:
        a, b = b, a + b
    return (decimal_integer % a) == 0
