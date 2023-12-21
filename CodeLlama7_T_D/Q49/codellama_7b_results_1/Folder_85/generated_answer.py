
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Initialize the Fibonacci sequence with the first two numbers
    fib_seq = [0, 1]
    # Iterate through the Fibonacci sequence until the 45th number is reached
    for i in range(len(fib_seq)):
        if fib_seq[i] == 45:
            # If the 45th number occurs in the Fibonacci sequence, check if the decimal integer is divisible by it
            if decimal_int % fib_seq[i] == 0:
                return True

    return False
