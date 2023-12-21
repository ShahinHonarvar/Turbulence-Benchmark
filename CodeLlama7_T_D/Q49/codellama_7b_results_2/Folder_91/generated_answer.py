
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_integer = int(binary_string, 2)
    # Initialize the Fibonacci sequence with the first two terms
    fib1 = 0
    fib2 = 1

    # Loop through the decimal integer and check if it is divisible by each term in the Fibonacci sequence
    for i in range(len(str(decimal_integer)))):
        digit = str(decimal_integer)[i]
        if digit == '1':
            if decimal_integer % fib1 == 0 or decimal_integer % fib2 == 0:
                return True

        else:

            fib3 = fib1 + fib2

            fib1 = fib2

            fib2 = fib3

    # If the loop completes without returning True, then the decimal integer is not divisible by any term in the Fibonacci sequence
    return False
