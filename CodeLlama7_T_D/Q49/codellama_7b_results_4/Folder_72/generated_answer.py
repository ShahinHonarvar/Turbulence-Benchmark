
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Initialize variables for the Fibonacci sequence
    a = 0
    b = 1
    # Loop through the numbers in the Fibonacci sequence until we reach the 175th number
    for i in range(174):
        c = a + b
        a = b
        b = c

    # Check if the decimal integer is divisible by the 175th number in the Fibonacci sequence
    if decimal_integer % b == 0:
        return True

    else:

        return False
