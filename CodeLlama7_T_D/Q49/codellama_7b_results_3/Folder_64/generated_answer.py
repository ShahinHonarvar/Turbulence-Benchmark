
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the Fibonacci number at the appropriate index
    fib_index = (decimal_integer % 10) - 1
    fib_number = fibonacci_sequence[fib_index]
    # Check if the decimal integer is divisible by the Fibonacci number
    return decimal_integer % fib_number == 0
