
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Initialize the Fibonacci sequence with the first two numbers
    fib1 = 0
    fib2 = 1

    # Iterate through the Fibonacci sequence until we find a number that is divisible by 120
    while True:
        if (decimal_integer % fib1) == 0 and (decimal_integer % fib2) == 0:
            return True
