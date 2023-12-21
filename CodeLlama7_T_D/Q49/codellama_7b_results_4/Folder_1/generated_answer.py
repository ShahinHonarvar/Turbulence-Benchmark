
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Initialize variables for the Fibonacci sequence
    fib0 = 0
    fib1 = 1
    fib2 = 1

    # Iterate through the digits of the decimal integer
    # and calculate the corresponding number in the Fibonacci sequence
    for digit in str(decimal_int):
        if digit == '1':
            fib0, fib1 = fib1, fib0 + fib1
        elif digit == '2':
            fib0, fib1 = fib1, fib0 + fib1 + fib2
        else:
            pass

    # Check if the integer corresponding to the given binary string is divisible by the 90th number in the Fibonacci sequence
    if decimal_int % fib2 == 0:
        return True

    else:

        return False
