
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to decimal integer
    decimal_integer = int(binary_representation, 2)
    # Initialize Fibonacci sequence with first two numbers
    fibonacci_sequence = [0, 1]
    # Calculate the 114th number in the Fibonacci sequence
    for i in range(113):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i+1])
    # Check if decimal integer is divisible by 114th number in the Fibonacci sequence
    return (decimal_integer % fibonacci_sequence[113]) == 0
