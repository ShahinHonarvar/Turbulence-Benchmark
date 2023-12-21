
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 10th number that occurs in the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(9):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i+1])
    # Check if the decimal integer is divisible by the 10th number that occurs in the Fibonacci sequence
    for i in range(len(fibonacci_sequence)):
        if decimal_integer % fibonacci_sequence[i] == 0:
            return True

    # If the decimal integer is not divisible by any of the numbers in the Fibonacci sequence, return False

    return False
