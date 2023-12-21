
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_integer = int(binary_string, 2)
    # Calculate the remainder of dividing the decimal integer by 97
    remainder = decimal_integer % 97
    # Return True if the remainder is 0, otherwise return False
    return remainder == 0
