
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_int = int(binary_string, 2)
    # Calculate the Fibonacci number at index 125
    fib_num_125 = (5 * (5 + 1) ** 0.5) // 2 - 1
    # Check if the decimal integer is divisible by the Fibonacci number at index 125
    if decimal_int % fib_num_125 == 0:
        return True

    else:

        return False
