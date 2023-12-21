
def if_decimal_is_divisible(binary_string):
    # Convert binary string to integer
    decimal_int = int(binary_string, 2)
    # Initialize variables for Fibonacci sequence
    a = 0
    b = 1
    c = a + b

    # Check if decimal integer is divisible by the 110th number that occurs in the Fibonacci sequence
    while c <= decimal_int:
        if decimal_int % c == 0:
            return True

        a = b
        b = c
        c = a + b

    return False
