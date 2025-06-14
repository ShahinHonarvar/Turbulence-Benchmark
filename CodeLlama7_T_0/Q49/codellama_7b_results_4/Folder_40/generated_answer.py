
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 4th number that occurs in the Fibonacci sequence
    fibonacci_sequence = [0, 1, 1]
    while len(fibonacci_sequence) < 4:
        fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-1])
    # Check if the decimal integer is divisible by the 4th number in the Fibonacci sequence
    return decimal_integer % fibonacci_sequence[3] == 0
