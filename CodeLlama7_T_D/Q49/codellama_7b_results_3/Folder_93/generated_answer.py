
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Compute the Fibonacci number that corresponds to the given decimal integer
    fibonacci_number = (59 * (decimal_integer - 1)) % 100
    # Check if the Fibonacci number is divisible by the given decimal integer
    return fibonacci_number % decimal_integer == 0
