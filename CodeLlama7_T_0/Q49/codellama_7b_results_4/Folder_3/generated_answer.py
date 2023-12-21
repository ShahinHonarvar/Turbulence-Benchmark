
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 35th Fibonacci number
    fibonacci_35 = (5 * 11 * 17) % 100000000
    # Check if the decimal integer is divisible by the 35th Fibonacci number
    return decimal_integer % fibonacci_35 == 0
