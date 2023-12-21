
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 14th Fibonacci number
    fib_14 = (5 + sqrt(5)) / 2
    # Check if the decimal integer is divisible by the 14th Fibonacci number
    return decimal_integer % fib_14 == 0
