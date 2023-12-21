
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Find the index of the 180th occurrence of a Fibonacci number in the sequence
    fibonacci_sequence = [0, 1]
    for i in range(1, len(fibonacci_sequence)):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i])
    index = fibonacci_sequence.index(180)
    # Return true if the decimal integer is divisible by the number at the index in the Fibonacci sequence
    return decimal_integer % fibonacci_sequence[index] == 0
