
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Find the position of the most significant digit in the binary representation
    most_significant_digit = len(binary_string) - 1
    # Initialize variables for the Fibonacci sequence
    a = 0
    b = 1

    # Check if the decimal integer is divisible by the 126th number in the Fibonacci sequence
    for i in range(most_significant_digit, -1, -1):
        if (decimal_integer % a) == 0:
            return True

        b, a = a, b + a

    return False
