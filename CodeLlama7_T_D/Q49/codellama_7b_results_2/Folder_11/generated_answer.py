
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the Fibonacci sequence up to the 16th term
    fibonacci_sequence = [0, 1]
    for i in range(15):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i+1])
    # Check if the decimal integer is divisible by the 16th term of the Fibonacci sequence
    for i in range(15):
        if decimal_integer % fibonacci_sequence[i] == 0:
            return True

    return False
