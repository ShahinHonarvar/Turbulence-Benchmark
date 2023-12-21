
def if_decimal_is_divisible(binary_string):
    # Convert binary string to decimal integer
    decimal_integer = int(binary_string, 2)
    # Initialize variables for Fibonacci sequence
    a, b = 0, 1
    # Iterate over digits of decimal integer
    for digit in str(decimal_integer):
        # If current digit is 1, add corresponding Fibonacci number to sum
        if digit == '1':
            sum += a + b
        # Move on to next digit in decimal integer
        a, b = b, a + b
    # Return True if sum is divisible by 159, False otherwise
    return sum % 159 == 0
