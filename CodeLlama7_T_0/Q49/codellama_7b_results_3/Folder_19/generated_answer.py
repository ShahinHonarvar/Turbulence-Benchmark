
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 29th Fibonacci number
    fibonacci_29 = 46368 * 10 ** 7 + 1
    # Check if the decimal integer is divisible by the 29th Fibonacci number
    return decimal_integer % fibonacci_29 == 0
