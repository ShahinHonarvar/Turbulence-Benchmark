
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_int = int(binary_string, 2)
    # Initialize the Fibonacci sequence with the first two numbers
    fib1, fib2 = 0, 1
    # Calculate the 64th number that occurs in the Fibonacci sequence
    fib64 = fib1 * fib2 * fib1 * fib2 * fib1 * fib2 * fib1 * fib2
    # Check if the decimal integer is divisible by the 64th number of the Fibonacci sequence
    return decimal_int % fib64 == 0
