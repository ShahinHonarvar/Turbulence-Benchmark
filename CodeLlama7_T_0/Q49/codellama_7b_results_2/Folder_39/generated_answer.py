
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 15th Fibonacci number
    fibonacci_15 = (5 * 13 + 8) // 2
    # Check if the decimal integer is divisible by the 15th Fibonacci number
    return decimal_integer % fibonacci_15 == 0
