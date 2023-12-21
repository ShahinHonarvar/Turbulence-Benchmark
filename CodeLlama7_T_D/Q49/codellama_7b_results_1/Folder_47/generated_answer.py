
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_integer = int(binary_string, 2)
    # Calculate the position of the 94th number in the Fibonacci sequence
    fibonacci_sequence = [0, 1] + list(range(1, 100))
    position_of_94th_number = len(fibonacci_sequence) - 2
    # Check if the decimal integer is divisible by the 94th number in the Fibonacci sequence
    if decimal_integer % fibonacci_sequence[position_of_94th_number] == 0:
        return True

    else:

        return False
