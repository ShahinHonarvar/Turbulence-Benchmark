
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 10th number in the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(10):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    10th_number = fibonacci_sequence[9]
    # Check if the decimal integer is divisible by the 10th number in the Fibonacci sequence
    if (decimal_integer % 10th_number) == 0:
        return True

    else:

        return False
