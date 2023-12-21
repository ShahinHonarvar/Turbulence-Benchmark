
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Get the remainder when dividing by the 134th Fibonacci number (which is 10946)
    remainder = decimal_integer % 10946
    # Return True if the remainder is 0, otherwise return False
    return remainder == 0
