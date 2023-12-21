
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_int = int(binary_string, 2)
    # Get the most significant digit in the decimal representation of the integer
    msb = str(decimal_int)[0]
    # Check if the most significant digit is 0 or 1
    if msb == '0' or msb == '1':
        return True

    else:

        return False
