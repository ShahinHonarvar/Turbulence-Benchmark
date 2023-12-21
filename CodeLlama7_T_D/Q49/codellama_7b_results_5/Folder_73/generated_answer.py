
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    decimal_int = int(binary_repr, 2)
    # Check if the integer is divisible by the 164th number that occurs in the Fibonacci sequence
    return (decimal_int % fibonacci_sequence[163]) == 0
