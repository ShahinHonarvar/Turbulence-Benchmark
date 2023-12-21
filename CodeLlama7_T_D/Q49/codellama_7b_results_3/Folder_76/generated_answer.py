
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to decimal
    decimal = int(binary_representation, 2)
    # Initialize variables for Fibonacci sequence
    a, b = 0, 1
    # Calculate Fibonacci sequence until the 188th number is reached
    while len(str(a)) < 188:
        a, b = b, a + b
    # Check if decimal integer is divisible by the 188th number of the Fibonacci sequence
    return decimal % a == 0
