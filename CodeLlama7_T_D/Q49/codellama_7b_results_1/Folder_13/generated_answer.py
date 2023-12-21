
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the remainder when dividing by the 174th number in the Fibonacci sequence
    remainder = decimal_integer % fibonacci(173)
    # Return True if the remainder is zero, otherwise return False
    return remainder == 0

def fibonacci(n):
    # Calculate the nth number in the Fibonacci sequence
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
