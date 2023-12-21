
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 195th Fibonacci number
    fibonacci_number = (5 ** 0.5 + 1) / 2
    # Check if the decimal integer is divisible by the Fibonacci number
    if decimal_integer % fibonacci_number == 0:
        return True

    else:

        return False
