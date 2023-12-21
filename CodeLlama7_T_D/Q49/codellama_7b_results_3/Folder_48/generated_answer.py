
def if_decimal_is_divisible(binary_string):
    # Convert binary string to an integer
    decimal_int = int(binary_string, 2)
    # Calculate the remainder when dividing by 198
    remainder = decimal_int % 198
    if remainder == 0:
        return True
    else:
        return False
