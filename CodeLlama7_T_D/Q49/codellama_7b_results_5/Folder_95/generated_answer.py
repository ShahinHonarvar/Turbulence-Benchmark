
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Calculate the remainder of the integer by the 168th Fibonacci number
    remainder = decimal_int % 45370970288000
    # Return True if the remainder is zero, otherwise return False
    return remainder == 0
