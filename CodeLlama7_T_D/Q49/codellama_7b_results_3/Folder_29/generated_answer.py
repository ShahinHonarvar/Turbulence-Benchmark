
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to decimal integer
    decimal_integer = int(binary_representation, 2)
    # Find the index of the 117th occurrence of the number that occurs in the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(len(fibonacci_sequence)):
        if decimal_integer % fibonacci_sequence[i] == 0:
            # Check if the number is divisible by the 117th occurrence of the Fibonacci sequence
            if i == len(fibonacci_sequence) - 117:
                return True

    return False
