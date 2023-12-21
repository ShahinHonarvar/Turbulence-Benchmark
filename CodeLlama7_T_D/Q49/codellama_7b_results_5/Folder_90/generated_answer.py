
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the Fibonacci sequence up to the 177th term
    fibonacci_sequence = [0, 1] + [fibonacci_sequence[i-1] + fibonacci_sequence[i-2] for i in range(2, 178)]
    # Check if the decimal integer is divisible by the 177th term of the Fibonacci sequence
    return decimal_integer % fibonacci_sequence[176] == 0
