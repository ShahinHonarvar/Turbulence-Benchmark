
def if_decimal_is_divisible(binary_string):
    # convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # find the position of the 19th Fibonacci number in the binary representation of the integer
    fibonacci_position = (decimal_integer).bit_length() - 1
    # check if the corresponding bit in the binary representation is set
    if (decimal_integer & (1 << fibonacci_position)) != 0:
        return True

    else:

        return False
