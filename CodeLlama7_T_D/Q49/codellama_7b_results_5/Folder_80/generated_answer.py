
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 179th number that occurs in the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < 179:
        fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-1])
    # Check if the decimal integer is divisible by the 179th number in the Fibonacci sequence
    if decimal_integer % fibonacci_sequence[178] == 0:
        return True

    else:

        return False
