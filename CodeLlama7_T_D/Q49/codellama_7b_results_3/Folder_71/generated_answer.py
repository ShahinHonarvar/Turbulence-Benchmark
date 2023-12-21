
def if_decimal_is_divisible(binary_rep):
    # Convert the binary representation to a decimal integer
    decimal = int(binary_rep, 2)
    # Calculate the remainder of dividing by 147
    remainder = decimal % 147
    # Return True if the remainder is equal to 0
    return (remainder == 0)
