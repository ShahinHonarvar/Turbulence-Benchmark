
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Get the Fibonacci sequence up to the 46th number
    fibonacci_sequence = [0, 1] + [fibonacci_sequence[i] + fibonacci_sequence[i+1] for i in range(len(fibonacci_sequence)-1)][:45]
    # Check if the decimal integer is divisible by the 46th number of the Fibonacci sequence
    return decimal_integer % fibonacci_sequence[45] == 0
