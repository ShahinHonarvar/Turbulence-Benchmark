
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    decimal_int = int(binary_repr, 2)
    # Initialize variables for the Fibonacci sequence
    a = 0
    b = 1

    # Iterate over the digits of the decimal integer
    for digit in str(decimal_int):
        # Check if the current digit is divisible by 27
        if int(digit) % 27 == 0:
            # If it is, return True
            return True

        # Otherwise, increment the Fibonacci sequence variables
        a, b = b, a + b

    # If we reach this point, all digits of the decimal integer were not divisible by 27
    return False
