
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 110th Fibonacci number
    fibonacci_110 = (5 * 110 + 640) // 10
    # Check if the decimal integer is divisible by the 110th Fibonacci number
    return decimal_integer % fibonacci_110 == 0
