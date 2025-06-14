
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation string to an integer
    decimal_integer = int(binary_representation, 2)
    # Check if the decimal integer is divisible by the 114th Fibonacci number
    if (decimal_integer % fibonacci(113)) == 0:
        return True

    else:

        return False

# Define the fibonacci function to calculate the 114th Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n

    else:

        return fibonacci(n-1) + fibonacci(n-2)
