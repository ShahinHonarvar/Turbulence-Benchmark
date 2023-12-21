
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal_int = int(binary_string, 2)
    # Calculate the 27th Fibonacci number
    fibonacci_27 = fibonacci(26)
    # Check if the decimal integer is divisible by the 27th Fibonacci number
    if decimal_int % fibonacci_27 == 0:
        return True

    else:

        return False

def fibonacci(n):

    if n <= 1:

        return n

    else:

        return fibonacci(n - 1) + fibonacci(n - 2)
