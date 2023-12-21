
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Initialize the Fibonacci sequence with the first two numbers
    fibonacci_seq = [0, 1]
    # Loop through the Fibonacci sequence until we find the 127th number that is divisible by the decimal integer
    for i in range(126):
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
        if (decimal_int % fibonacci_seq[i]) == 0:
            return True

    # If we reach this point, it means that the decimal integer is not divisible by any number in the Fibonacci sequence, so we return False
    return False
