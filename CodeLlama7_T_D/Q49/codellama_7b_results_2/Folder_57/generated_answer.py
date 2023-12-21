
def if_decimal_is_divisible(binary_representation):
    # Convert the binary representation to an integer
    decimal_integer = int(binary_representation, 2)
    # Calculate the Fibonacci sequence upto the 80th number
    fibonacci_sequence = [0, 1]
    for i in range(2, 80):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    # Check if the decimal integer is divisible by the 80th number of the Fibonacci sequence
    return decimal_integer % fibonacci_sequence[79] == 0
