
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_int = int(binary_string, 2)
    # Calculate the 108th Fibonacci number
    fib_108 = ((5**0.5 + 1) / 2)**108
    # Check if the decimal integer is divisible by the 108th Fibonacci number
    if (decimal_int % fib_108) == 0:
        return True

    else:

        return False
