
def if_decimal_is_divisible(binary_representation):
    # Convert binary representation to decimal integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the 17th Fibonacci number
    fibonacci_sequence = [0, 1]
    for i in range(17):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i+1])
    # Check if decimal integer is divisible by the 17th Fibonacci number
    return decimal_integer % fibonacci_sequence[16] == 0
