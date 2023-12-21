
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to a decimal integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the 100th number that occurs in the Fibonacci sequence
    fibonacci_sequence = [0, 1, 1]
    for i in range(3, len(fibonacci_sequence)):
        fibonacci_sequence.append(fibonacci_sequence[i - 2] + fibonacci_sequence[i - 1])
    # Check if the decimal integer is divisible by the 100th number in the Fibonacci sequence
    return decimal_integer % fibonacci_sequence[-1] == 0
