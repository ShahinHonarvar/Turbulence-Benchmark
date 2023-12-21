
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Initialize a list to store the Fibonacci sequence
    fib_sequence = [0]
    # Iterate until the 180th number occurs in the sequence
    while len(fib_sequence) < 180:
        # Add the next two numbers in the sequence
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]))
    # Check if the decimal integer is divisible by any number in the Fibonacci sequence
    for num in fib_sequence:
        if decimal_integer % num == 0:
            return True

    return False
