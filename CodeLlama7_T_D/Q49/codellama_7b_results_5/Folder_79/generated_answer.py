
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Get the Fibonacci sequence up to the 13th term
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    # Check if the decimal integer is divisible by the 13th Fibonacci number
    return decimal_integer % fibonacci_sequence[12] == 0
