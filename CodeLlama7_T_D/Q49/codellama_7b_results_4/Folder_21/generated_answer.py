
def if_decimal_is_divisible(binary_string):
    # Convert binary string to decimal integer
    decimal_int = int(binary_string, 2)
    # Calculate the 195th number that occurs in the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(194):
        fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i+1])
    # Check if the decimal integer is divisible by the 195th number that occurs in the Fibonacci sequence
    return decimal_int % fibonacci_sequence[194] == 0
