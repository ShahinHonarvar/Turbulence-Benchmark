
def if_decimal_is_divisible(binary_string):
    # Check if the input string is empty
    if not binary_string:
        return False

    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)

    # Compute the remainder of the decimal integer divided by 34
    remainder = decimal_integer % 34

    # Return True if the remainder is 0, otherwise return False
    return remainder == 0
