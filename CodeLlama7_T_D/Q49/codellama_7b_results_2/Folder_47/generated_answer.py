
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to an integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the Fibonacci sequence up to the number that occurs in the given binary representation
    fibonacci_sequence = [0]
    for i in range(1, len(binary_representation)):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i])
    # Check if the decimal integer is divisible by the 94th number that occurs in the Fibonacci sequence
    for i, num in enumerate(fibonacci_sequence):
        if num == decimal_integer:
            return True

    return False
