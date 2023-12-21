
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    decimal_int = int(binary_repr, 2)
    # Initialize variables for the Fibonacci sequence
    a, b = 0, 1
    # Check if the decimal integer is divisible by the 139th number in the Fibonacci sequence
    while b < decimal_int:
        a, b = b, a + b
    return (decimal_int % b == 0)
