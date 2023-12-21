
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the Fibonacci sequence index
    fibonacci_index = (decimal_integer // 104) + 1
    # Check if the decimal integer is divisible by the corresponding Fibonacci number
    return decimal_integer % fibonacci_sequence[fibonacci_index] == 0
