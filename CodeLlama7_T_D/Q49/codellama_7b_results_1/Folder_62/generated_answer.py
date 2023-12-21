 def if_decimal_is_divisible(binary_repr):
    # convert the binary representation string to an integer
    decimal_int = int(binary_repr, 2)
    # calculate the number of digits in the Fibonacci sequence that are less than or equal to the given decimal integer
    num_digits = sum([1 for i in range(50) if decimal_int // (130 ** i) > 0])
    # calculate the remainder when the given decimal integer is divided by the 130th number that occurs in the Fibonacci sequence
    remainder = decimal_int % (130 ** num_digits)
    # return true if the remainder is zero, otherwise return false
    return remainder == 0
