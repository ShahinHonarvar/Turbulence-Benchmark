
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to an integer
    decimal_integer = int(binary_representation, 2)
    # Initialize the Fibonacci sequence with the first two numbers
    fibonacci_sequence = [0, 1]
    # Iterate through the Fibonacci sequence and find the 76th number
    for i in range(75):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i+1])
    # Check if the decimal integer is divisible by the 76th Fibonacci number
    return decimal_integer % fibonacci_sequence[75] == 0
