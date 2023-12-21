
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_integer = int(binary_string, 2)
    # Initialize variables for the Fibonacci sequence
    a = 0
    b = 1
    # Calculate the 15th number that occurs in the Fibonacci sequence
    for i in range(14):
        a, b = b, a + b
    # Check if the decimal integer is divisible by the 15th number
    return decimal_integer % b == 0
