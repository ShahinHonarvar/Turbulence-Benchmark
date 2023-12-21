
def if_decimal_is_divisible(binary_string):
    # convert binary string to an integer
    decimal_int = int(binary_string, 2)
    # find the 115th Fibonacci number
    a, b = 0, 1
    for _ in range(115):
        a, b = b, a + b
    # check if the decimal integer is divisible by the 115th Fibonacci number
    return decimal_int % a == 0
