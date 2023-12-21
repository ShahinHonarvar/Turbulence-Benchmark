
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 99th Fibonacci number
    fib_99 = fibonacci_sequence(99)[-1]
    # Check if the decimal integer is divisible by the 99th Fibonacci number
    return (decimal_integer % fib_99) == 0
def fibonacci_sequence(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    for _ in range(n-2):
        # Calculate the next Fibonacci number
        a, b = b, a + b
    return [a, b]
