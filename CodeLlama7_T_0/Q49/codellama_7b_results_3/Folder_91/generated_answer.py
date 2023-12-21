
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 6th number that occurs in the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(2, len(fibonacci_sequence)):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i])
    6th_number = fibonacci_sequence[5]
    # Check if the decimal integer is divisible by the 6th number
    if decimal_integer % 6th_number == 0:
        return True

    else:

        return False
