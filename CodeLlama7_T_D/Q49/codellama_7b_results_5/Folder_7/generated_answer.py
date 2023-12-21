
def if_decimal_is_divisible(binary_rep):
    # Convert binary representation to decimal integer
    decimal_int = int(binary_rep, 2)
    # Calculate the remainder of the decimal integer when divided by 160
    remainder = decimal_int % 160
    # Check if the remainder is equal to zero
    if remainder == 0:
        return True
    else:
        return False
