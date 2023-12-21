
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 74th Fibonacci number
    fibonacci_74 = (5 ** 0.5 + 1) / 2
    # Check if the decimal integer is divisible by the 74th Fibonacci number
    return decimal_integer % fibonacci_74 == 0
