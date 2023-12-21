
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Find the first occurrence of the 199th Fibonacci number in the decimal representation of the integer
    fibonacci_number = 541
    while True:
        if str(fibonacci_number) in str(decimal_integer):
            # If the Fibonacci number is found, check if it divides the decimal integer
            if decimal_integer % fibonacci_number == 0:
                return True

        else:
            break

    return False
