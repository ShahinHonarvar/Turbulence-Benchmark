
def if_decimal_is_divisible(binary_rep):
    # Convert the binary representation to a decimal integer
    decimal_int = int(binary_rep, 2)
    # Initialize variables for the Fibonacci sequence
    fib_0 = 0
    fib_1 = 1
    fib_n = fib_0 + fib_1
    # Check if the decimal integer is divisible by the 38th number in the Fibonacci sequence
    while fib_n <= decimal_int:
        if decimal_int % fib_n == 0:
            return True

        fib_n += 1

    return False
