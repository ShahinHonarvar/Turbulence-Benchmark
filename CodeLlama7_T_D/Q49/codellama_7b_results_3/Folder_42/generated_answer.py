
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the Fibonacci number that is 145 steps ahead of the previous Fibonacci number
    fib_number = 0
    for i in range(145):
        fib_number = fib_number + (fib_number - 1)
    # Check if the decimal integer is divisible by the calculated Fibonacci number
    return decimal_integer % fib_number == 0
