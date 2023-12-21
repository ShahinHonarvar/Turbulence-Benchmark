 def if_decimal_is_divisible(binary_rep):
    # Convert the binary representation string to an integer
    decimal = int(binary_rep, 2)
    # Initialize variables for the Fibonacci sequence
    a, b = 0, 1
    # Iterate until the 80th number occurs in the Fibonacci sequence
    while b < 80:
        a, b = b, a + b
    # Check if the decimal integer is divisible by the 80th number
    return decimal % b == 0
