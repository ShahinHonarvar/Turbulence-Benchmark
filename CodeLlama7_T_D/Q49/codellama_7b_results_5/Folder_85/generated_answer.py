
def if_decimal_is_divisible(binary_rep):
    # Convert the binary representation string to an integer
    decimal_int = int(binary_rep, 2)
    # Initialize variables for the Fibonacci sequence
    a = 0
    b = 1

    # Iterate through the Fibonacci sequence until we reach the 45th number
    while len(str(a)) < 45:
        c = a + b
        a = b
        b = c

    # Check if the decimal integer is divisible by the 45th number in the Fibonacci sequence
    if (decimal_int % int(str(a)[-45:]))) == 0:
        return True

    else:

        return False
