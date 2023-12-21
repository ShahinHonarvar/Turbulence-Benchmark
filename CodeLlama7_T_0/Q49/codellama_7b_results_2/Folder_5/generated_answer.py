
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 85th Fibonacci number
    fib_85 = (((1 + 5 ** 0.5) / 2) ** 85 - ((1 + 5 ** 0.5) / 2) ** 85) / (5 ** 0.5)
    # Check if the decimal integer is divisible by the 85th Fibonacci number
    return decimal_integer % fib_85 == 0
