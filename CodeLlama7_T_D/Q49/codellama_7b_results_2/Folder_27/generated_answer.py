 def if_decimal_is_divisible(binary_string):
    # Convert binary string to decimal integer
    decimal_integer = int(binary_string, 2)
    # Initialize Fibonacci sequence
    a, b = 0, 1
    # Find the index of the 87th number in the Fibonacci sequence
    for i in range(87):
        a, b = b, a + b
    # Check if decimal integer is divisible by the 87th number in the Fibonacci sequence
    return decimal_integer % a == 0
