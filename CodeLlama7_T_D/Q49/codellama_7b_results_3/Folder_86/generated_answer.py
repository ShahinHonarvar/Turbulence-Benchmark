
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_integer = int(binary_string, 2)
    # Initialize variables for the Fibonacci sequence
    fib1 = 0
    fib2 = 1
    # Calculate the 135th number in the Fibonacci sequence
    for i in range(134):
        temp = fib1 + fib2
        fib1 = fib2
        fib2 = temp

    # Check if the decimal integer is divisible by the 135th number in the Fibonacci sequence
    if (decimal_integer % fib2) == 0:
        return True

    else:

        return False
