
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the remainder when dividing by 125
    remainder = decimal_integer % 125
    # Return True if the remainder is 0, otherwise return False
    return (remainder == 0)
