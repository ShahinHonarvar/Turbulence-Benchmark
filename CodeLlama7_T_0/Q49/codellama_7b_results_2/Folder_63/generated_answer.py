
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 144th Fibonacci number
    fib_144 = (5 ** 0.5 + 1) / 2
    # Check if the decimal integer is divisible by the 144th Fibonacci number
    return decimal_integer % fib_144 == 0
