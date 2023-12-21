
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_integer = int(binary_string, 2)
    # Initialize the Fibonacci sequence with 0 and 1
    fibonacci_sequence = [0, 1]
    # Calculate the Fibonacci sequence up to the 66th number
    while len(fibonacci_sequence) <= 66:
        fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-1])
    # Check if the decimal integer is divisible by the 66th Fibonacci number
    return decimal_integer % fibonacci_sequence[65] == 0
