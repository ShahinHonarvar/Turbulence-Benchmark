
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Check if the decimal integer is divisible by the 176th Fibonacci number
    fibonacci_175 = 46600
    return decimal_integer % fibonacci_175 == 0
