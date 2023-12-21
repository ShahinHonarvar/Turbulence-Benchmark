 def if_decimal_is_divisible(binary_string):
    # Convert binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Check if the integer is divisible by 117
    return decimal_integer % 117 == 0
