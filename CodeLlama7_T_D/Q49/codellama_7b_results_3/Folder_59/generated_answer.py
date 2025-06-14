
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Initialize variables for Fibonacci sequence
    a, b = 0, 1
    # Calculate the number of digits in the binary string
    num_digits = len(binary_string)
    # Loop through each digit in the binary string and calculate the corresponding Fibonacci number
    for i in range(num_digits):
        if (i + 1) % 7 == 0:
            a, b = b, a + b
    # Check if the decimal integer is divisible by the Fibonacci number
    return True if decimal_int % a == 0 else False
