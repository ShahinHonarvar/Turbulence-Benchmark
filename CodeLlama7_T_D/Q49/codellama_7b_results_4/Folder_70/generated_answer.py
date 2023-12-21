
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Calculate the Fibonacci sequence for the given decimal integer
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] <= decimal_int:
        fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-3])
    # Check if the given decimal integer is divisible by the 137th number in the Fibonacci sequence
    return decimal_int % fibonacci_sequence[-1] == 0
