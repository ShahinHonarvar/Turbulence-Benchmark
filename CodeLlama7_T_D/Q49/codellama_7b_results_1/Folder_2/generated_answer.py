
def if_decimal_is_divisible(binary_string):
    # Convert binary string to an integer
    decimal_int = int(binary_string, 2)
    # Check if the decimal integer is divisible by the 125th number in the Fibonacci sequence
    fib_seq = [0, 1, 1, 2, 3, 5]
    for i in range(len(fib_seq)):
        if decimal_int % fib_seq[i] == 0:
            return True

    # If the loop completes without returning True, then the decimal integer is not divisible by the 125th number in the Fibonacci sequence
    return False
