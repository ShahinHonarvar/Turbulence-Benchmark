
def if_decimal_is_divisible(binary_representation):
    # convert binary representation to decimal integer
    decimal_integer = int(binary_representation, 2)
    # compute the 118th Fibonacci number
    a = 0
    b = 1
    for i in range(117):
        c = a + b
        a = b
        b = c

    # check if decimal integer is divisible by 118th Fibonacci number
    if decimal_integer % c == 0:
        return True

    else:
        return False
