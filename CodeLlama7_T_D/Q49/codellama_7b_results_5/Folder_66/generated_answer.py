
def if_decimal_is_divisible(binary_string):
    # Convert binary string to decimal integer
    decimal_int = int(binary_string, 2)
    # Initialize Fibonacci sequence with first two terms
    fib1, fib2 = 0, 1
    # Calculate the nth term of the Fibonacci sequence
    for _ in range(120):
        fib1, fib2 = fib2, fib1 + fib2
    # Check if decimal integer is divisible by nth term of the Fibonacci sequence
    return decimal_int % fib2 == 0
