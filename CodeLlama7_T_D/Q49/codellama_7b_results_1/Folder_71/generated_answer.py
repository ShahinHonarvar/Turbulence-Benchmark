
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the Fibonacci sequence index for the given decimal integer
    fibonacci_index = (decimal_integer // 60) % 147
    # Check if the Fibonacci sequence index is divisible by 147
    return fibonacci_index % 147 == 0
