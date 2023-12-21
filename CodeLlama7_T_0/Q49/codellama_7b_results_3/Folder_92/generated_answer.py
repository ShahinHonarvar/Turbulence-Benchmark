
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 7th Fibonacci number
    fibonacci_7 = (5 + sqrt(5)) / 2
    # Check if the decimal integer is divisible by the 7th Fibonacci number
    return decimal_integer % fibonacci_7 == 0
