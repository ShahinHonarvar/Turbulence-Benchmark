
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 27th Fibonacci number
    fibonacci_27 = (1.618033988749895 * 1e18) % 1e18
    # Check if the decimal integer is divisible by the 27th Fibonacci number
    return decimal_integer % fibonacci_27 == 0
