
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Find the 199th number that occurs in the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(198):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i + 1])
    # Check if the decimal integer is divisible by the 199th number that occurs in the Fibonacci sequence
    return decimal_integer % fibonacci_sequence[198] == 0
