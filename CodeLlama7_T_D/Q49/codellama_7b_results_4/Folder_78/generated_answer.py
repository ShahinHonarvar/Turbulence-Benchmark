
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Initialize variables for the Fibonacci sequence
    a, b = 0, 1
    # Check if the decimal integer is divisible by the 115th number that occurs in the Fibonacci sequence
    while b < decimal_integer:
        a, b = b, a + b
    return (b == decimal_integer)
