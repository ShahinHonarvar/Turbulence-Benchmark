
def if_decimal_is_divisible(binary_string):
    # Convert binary string to integer
    decimal_integer = int(binary_string, 2)
    # Initialize variables for Fibonacci sequence
    a = 0
    b = 1
    c = a + b

    # Check if decimal integer is divisible by the 108th number that occurs in the Fibonacci sequence
    while c < decimal_integer:
        a = b
        b = c
        c = a + b

    return (decimal_integer % c) == 0
