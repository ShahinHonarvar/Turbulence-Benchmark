
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_integer = int(binary_string, 2)
    # Get the Fibonacci sequence up to the 178th number
    fibonacci_sequence = [0, 1] + [fibonacci_sequence[i-1] + fibonacci_sequence[i-2] for i in range(2, 179)]
    # Check if the decimal integer is divisible by the 178th number of the Fibonacci sequence
    return decimal_integer % fibonacci_sequence[178] == 0
