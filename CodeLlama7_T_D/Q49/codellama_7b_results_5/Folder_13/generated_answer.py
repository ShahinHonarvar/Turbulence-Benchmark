
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 174th number in the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(1, 174):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i])
    # Check if the decimal integer is divisible by the 174th number in the Fibonacci sequence
    if decimal_integer % fibonacci_sequence[173] == 0:
        return True

    else:

        return False
