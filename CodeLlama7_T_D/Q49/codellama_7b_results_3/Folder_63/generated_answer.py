
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to decimal integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the remainder when dividing by 144
    remainder = decimal_integer % 144
    # Return True if remainder is zero, otherwise return False
    return remainder == 0
