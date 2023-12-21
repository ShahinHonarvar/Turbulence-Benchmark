
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Initialize variables for the Fibonacci sequence
    a, b = 0, 1
    # Check if the decimal integer is divisible by the 38th number in the Fibonacci sequence
    for i in range(37):
        a, b = b, a + b
    return decimal_int % a == 0
