
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to an integer
    decimal_integer = int(binary_representation, 2)
    # Find the 14th number that occurs in the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(14):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i+1])
    # Check if the decimal integer is divisible by the 14th number of the Fibonacci sequence
    return decimal_integer % fibonacci_sequence[14] == 0
