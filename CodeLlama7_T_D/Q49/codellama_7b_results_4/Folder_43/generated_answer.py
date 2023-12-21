
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to decimal integer
    decimal_integer = int(binary_representation, 2)
    # Initialize Fibonacci sequence with first two numbers
    fibonacci_sequence = [0, 1]
    # Iterate over the decimal integer and check for divisibility by 77th number in Fibonacci sequence
    for i in range(len(str(decimal_integer)))):
        if (i + 1) % 77 == 0:
            # If divisible, return true
            return True

    # If not divisible, return false
    return False
