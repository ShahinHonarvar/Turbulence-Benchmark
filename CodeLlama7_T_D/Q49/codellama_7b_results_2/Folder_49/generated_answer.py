
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 95th Fibonacci number
    fibonacci_95 = calculate_fibonacci_number(95)
    # Check if the decimal integer is divisible by the 95th Fibonacci number
    if (decimal_integer % fibonacci_95) == 0:
        return True

    else:

        return False

def calculate_fibonacci_number(n):

    # Calculate the nth Fibonacci number using the Binet's formula

    return int((5 * pow(phi, n - 1)) / (2 * pi)))
