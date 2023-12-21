
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation to a decimal integer
    decimal_int = int(binary_repr, 2)
    # Calculate the Fibonacci number that occurs in the decimal integer's representation
    fibonacci_number = (decimal_int % 60) - 1
    # Check if the Fibonacci number is divisible by the 60th number that occurs in the Fibonacci sequence
    return fibonacci_number % 60 == 0
