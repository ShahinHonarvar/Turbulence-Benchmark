
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Find the index of the 29th occurrence of the number in the Fibonacci sequence
    fib_index = (29 - 1) % len(fibonacci_sequence)
    # Get the number at that index from the Fibonacci sequence
    number = fibonacci_sequence[fib_index]
    # Check if the decimal integer is divisible by the number in the Fibonacci sequence
    return (decimal_int % number == 0)
