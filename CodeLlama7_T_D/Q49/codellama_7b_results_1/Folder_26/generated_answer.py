
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Initialize variables for Fibonacci sequence
    a = 0
    b = 1

    # Check if the decimal integer is divisible by the 138th number that occurs in the Fibonacci sequence
    while a < decimal_int:
        a, b = b, a + b

    return (decimal_int % a) == 0
