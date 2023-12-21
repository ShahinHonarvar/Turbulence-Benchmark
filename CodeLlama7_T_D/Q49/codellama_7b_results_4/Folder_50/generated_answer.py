 def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to decimal integer
    decimal_integer = int(binary_representation, 2)
    # Get the Fibonacci sequence up to the 119th term
    fibonacci_sequence = [0, 1]
    for i in range(2, 120):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    # Check if the decimal integer is divisible by the 119th term of the Fibonacci sequence
    return decimal_integer % fibonacci_sequence[118] == 0
