
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to decimal integer
    decimal_integer = int(binary_representation, 2)
    # Check if decimal integer is divisible by 105th Fibonacci number
    if decimal_integer % fibonacci(105) == 0:
        return True

    else:

        return False

# Define function to compute Fibonacci numbers
def fibonacci(n):
    if n <= 1:
        return n

    else:

        return fibonacci(n-1) + fibonacci(n-2)
