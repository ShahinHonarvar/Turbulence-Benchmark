
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation to an integer
    decimal_int = int(binary_repr, 2)
    # Initialize variables for the Fibonacci sequence
    a, b = 0, 1
    # Check if the decimal integer is divisible by the 80th number that occurs in the Fibonacci sequence
    while a < decimal_int:
        a, b = b, a + b
    return decimal_int % a == 0
