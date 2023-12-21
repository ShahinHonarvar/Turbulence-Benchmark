
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 28th Fibonacci number
    fibonacci_28 = (5 ** 0.5 + 1) / 2
    # Check if the decimal integer is divisible by the 28th Fibonacci number
    return decimal_integer % fibonacci_28 == 0
