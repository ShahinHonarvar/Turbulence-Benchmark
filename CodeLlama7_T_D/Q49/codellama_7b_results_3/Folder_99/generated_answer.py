
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the remainder when dividing by 109
    remainder = decimal_integer % 109
    # Return True if the remainder is 0, otherwise return False
    return remainder == 0
