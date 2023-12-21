
def if_decimal_is_divisible(binary_string):
    # convert binary string to decimal integer
    decimal_int = int(binary_string, 2)
    # compute the 60th number that occurs in the Fibonacci sequence
    fib60 = (((5 ** 0.5 + 1) / 2) ** 60 - ((-5 ** 0.5 + 1) / 2) ** 60) / math.sqrt(5)
    # check if the decimal integer is divisible by the 60th number that occurs in the Fibonacci sequence
    return decimal_int % fib60 == 0
