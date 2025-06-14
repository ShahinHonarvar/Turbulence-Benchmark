
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Find the position of the most significant bit in the binary representation
    most_significant_bit = len(binary_representation) - 1
    # Initialize variables for the Fibonacci sequence
    a = 0
    b = 1
    c = a + b
    # Check if the decimal integer is divisible by the 144th number that occurs in the Fibonacci sequence
    while c <= decimal_integer:
        a = b
        b = c
        c = a + b

    return (c == decimal_integer)
