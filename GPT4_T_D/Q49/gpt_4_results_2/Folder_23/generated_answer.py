
def if_decimal_is_divisible(binary_string):
    # Convert binary string to decimal
    decimal = int(binary_string, 2)
    # Initializing the Fibonacci sequence
    first, second = 0, 1
    fib_number = 1
    # Generating the 48th Fibonacci number
    while fib_number < 48:
        first, second = second, first + second
        fib_number += 1
    # Checking if the decimal number is divisible by the 48th Fibonacci number
    return decimal % second == 0
