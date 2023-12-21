
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_int = int(binary_string, 2)
    # Calculate the 188th Fibonacci number
    fib_188 = (5 ** 0.5 + 1) / 2
    # Check if the decimal integer is divisible by the 188th Fibonacci number
    if decimal_int % fib_188 == 0:
        return True

    else:

        return False
