
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 100th number in the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(2, 100):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    # Check if the decimal integer is divisible by the 100th number in the Fibonacci sequence
    for i in range(len(fibonacci_sequence)):
        if decimal_integer % fibonacci_sequence[i] == 0:
            return True

    # If the decimal integer is not divisible by any number in the Fibonacci sequence, return False

    return False
