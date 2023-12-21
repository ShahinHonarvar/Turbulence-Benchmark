
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 186th Fibonacci number
    fib_186 = (5 ** 0.5 + 1) / 2
    # Check if the decimal integer is divisible by the 186th Fibonacci number
    return decimal_integer % fib_186 == 0
