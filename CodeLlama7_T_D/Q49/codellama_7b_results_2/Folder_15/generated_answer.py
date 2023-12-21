
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the 9th number that occurs in the Fibonacci sequence
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13]
    ninth_number = fibonacci_sequence[9]
    # Check if the decimal integer is divisible by the 9th number in the Fibonacci sequence
    return decimal_integer % ninth_number == 0
