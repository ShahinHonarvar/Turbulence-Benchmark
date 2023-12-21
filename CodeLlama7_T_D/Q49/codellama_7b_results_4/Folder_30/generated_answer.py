
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to decimal integer
    decimal_integer = int(binary_representation, 2)
    # Initialize variables for Fibonacci sequence
    a, b = 0, 1
    # Check if the decimal integer is divisible by the 186th number that occurs in the Fibonacci sequence
    for i in range(185):
        a, b = b, a + b
    return decimal_integer % a == 0
