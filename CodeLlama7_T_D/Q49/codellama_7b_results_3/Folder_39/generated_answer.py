
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to decimal integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the 15th number in the Fibonacci sequence
    fibonacci_sequence = [0, 1, 2, 3, 5]
    15th_number = fibonacci_sequence[14]
    # Check if the decimal integer is divisible by the 15th number in the Fibonacci sequence
    if decimal_integer % 15th_number == 0:
        return True
    else:
        return False
