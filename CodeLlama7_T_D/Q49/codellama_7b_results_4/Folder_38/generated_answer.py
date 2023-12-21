
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the 78th number that occurs in the Fibonacci sequence
    fibonacci_sequence = [0]
    for i in range(1, 78):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    # Check if the decimal integer is divisible by the 78th number that occurs in the Fibonacci sequence
    for num in fibonacci_sequence:
        if decimal_integer % num == 0:
            return True

    return False
