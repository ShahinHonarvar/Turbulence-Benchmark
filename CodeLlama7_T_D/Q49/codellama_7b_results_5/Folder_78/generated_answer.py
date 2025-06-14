
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Initialize a list to store the Fibonacci sequence numbers
    fibonacci_sequence = [0]
    # Generate the Fibonacci sequence up to the 115th number
    for i in range(116):
        fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-1])
    # Check if the decimal integer is divisible by any of the Fibonacci sequence numbers
    for num in fibonacci_sequence:
        if decimal_integer % num == 0:
            return True

    # If none of the Fibonacci sequence numbers divide evenly into the decimal integer, return False
    return False
