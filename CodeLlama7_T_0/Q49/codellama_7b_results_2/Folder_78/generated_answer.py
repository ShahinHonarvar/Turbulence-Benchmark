
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 115th Fibonacci number
    fib_115 = (((5 * math.sqrt(5)) + 1) / 2) ** 115
    # Check if the decimal integer is divisible by the 115th Fibonacci number
    return decimal_integer % fib_115 == 0
