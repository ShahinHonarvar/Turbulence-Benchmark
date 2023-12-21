
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Check if the decimal integer is divisible by the 135th number in the Fibonacci sequence
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i in range(len(fibonacci_sequence)):
        if decimal_integer % fibonacci_sequence[i] == 0:
            return True

    return False
