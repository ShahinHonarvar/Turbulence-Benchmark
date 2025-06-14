
def if_decimal_is_divisible(binary_string):
    # Convert binary string to decimal integer
    decimal_int = int(binary_string, 2)
    # Get the last occurrence of 1 in the binary representation
    last_one_index = binary_string.rfind('1')
    # Get the index of the 125th number that occurs in the Fibonacci sequence
    fibonacci_index = int(last_one_index / 3)
    # Check if the decimal integer is divisible by the 125th number that occurs in the Fibonacci sequence
    return (decimal_int % fibonacci_number) == 0
