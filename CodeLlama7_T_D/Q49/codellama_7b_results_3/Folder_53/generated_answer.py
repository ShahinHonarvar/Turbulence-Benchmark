
def if_decimal_is_divisible(binary_rep):
    # convert the binary representation to a decimal integer
    decimal = int(binary_rep, 2)
    # calculate the 64th number that occurs in the Fibonacci sequence
    fibonacci_64 = 46368 * 5**51 + 1220703125**51
    # check if the decimal integer is divisible by the 64th number of the Fibonacci sequence
    return decimal % fibonacci_64 == 0
