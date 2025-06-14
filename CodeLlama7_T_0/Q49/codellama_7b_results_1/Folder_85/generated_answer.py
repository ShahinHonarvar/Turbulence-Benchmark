
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Initialize variables for the Fibonacci sequence
    a = 0
    b = 1
    c = a + b

    # Check if the decimal integer is divisible by the 45th number in the Fibonacci sequence
    while c <= decimal_integer:
        if decimal_integer % c == 0:
            return True

        a = b
        b = c
        c = a + b

    return False
