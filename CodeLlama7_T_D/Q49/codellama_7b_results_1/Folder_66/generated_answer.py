
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_integer = int(binary_string, 2)
    # Calculate the remainder when the decimal integer is divided by the 120th Fibonacci number
    remainder = decimal_integer % fibonacci(120)
    # Return True if the remainder is equal to 0; otherwise return False
    return remainder == 0

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
