
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation string to an integer
    decimal_integer = int(binary_representation, 2)
    # Initialize the Fibonacci sequence with the first two numbers
    fib1 = 0
    fib2 = 1

    # Iterate through the Fibonacci sequence until we find a number that divides evenly into the decimal integer
    while True:
        if (decimal_integer % fib1) == 0 or (decimal_integer % fib2) == 0:
            return True
