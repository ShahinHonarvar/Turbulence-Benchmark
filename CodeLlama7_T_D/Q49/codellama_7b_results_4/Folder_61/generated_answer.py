
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Initialize variables to keep track of the Fibonacci sequence
    fib1 = 0
    fib2 = 1
    fib3 = 1
    # Check if the decimal integer is divisible by the 76th number in the Fibonacci sequence
    while fib3 < decimal_integer:
        fib1, fib2, fib3 = fib2, fib3, fib1 + fib2
    return (decimal_integer % fib3) == 0
