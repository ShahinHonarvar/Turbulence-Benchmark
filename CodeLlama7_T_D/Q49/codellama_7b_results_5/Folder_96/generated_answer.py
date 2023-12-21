
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Initialize the Fibonacci sequence with the first two terms
    fibonacci_sequence = [0, 1]
    # Calculate the Fibonacci sequence up to the 47th term
    for i in range(47):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i + 1])
    # Check if the decimal integer is divisible by the 47th Fibonacci number
    if decimal_integer % fibonacci_sequence[46] == 0:
        return True

    else:

        return False
