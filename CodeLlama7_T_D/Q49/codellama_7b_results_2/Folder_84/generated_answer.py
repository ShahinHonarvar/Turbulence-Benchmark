
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Calculate the 196th Fibonacci number
    fib_196 = ((5 ** 0.5 + 1) / 2) ** 196
    # Check if the decimal integer is divisible by the 196th Fibonacci number
    if (decimal_int % fib_196) == 0:
        return True

    else:

        return False
