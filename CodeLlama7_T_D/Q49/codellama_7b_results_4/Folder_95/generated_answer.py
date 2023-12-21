
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to an integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the Fibonacci number that corresponds to the given decimal integer
    fibonacci_number = (5 * decimal_integer ** 2 + 4 * decimal_integer - 4) // 168
    # Return true if the Fibonacci number is divisible by 168, otherwise return false
    return fibonacci_number % 168 == 0
