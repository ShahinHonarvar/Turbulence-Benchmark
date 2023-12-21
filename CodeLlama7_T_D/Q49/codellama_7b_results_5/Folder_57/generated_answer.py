
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Calculate the 80th Fibonacci number
    fib80 = (5 ** 0.5 + 1) / 2
    # Check if the decimal integer is divisible by the 80th Fibonacci number
    return decimal_int % fib80 == 0
