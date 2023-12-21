
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to decimal integer
    decimal_integer = int(binary_representation, 2)
    # Initialize variables for Fibonacci sequence
    a, b = 0, 1
    # Check if decimal integer is divisible by the 186th number in the Fibonacci sequence
    for i in range(decimal_integer):
        a, b = b, a + b
        if a == 185:
            return True

    return False
