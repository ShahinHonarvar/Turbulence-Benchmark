
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the Fibonacci sequence up to the 117th number
    fibonacci_sequence = [0] * 117
    for i in range(117):
        fibonacci_sequence[i] = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
    # Check if the decimal integer is divisible by the 117th number of the Fibonacci sequence
    for i in range(len(fibonacci_sequence)):
        if decimal_integer % fibonacci_sequence[i] == 0:
            return True

    return False
