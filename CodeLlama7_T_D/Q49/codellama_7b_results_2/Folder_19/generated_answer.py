
def if_decimal_is_divisible(binary_string):
    # Convert binary string to integer
    num = int(binary_string, 2)
    # Find the 29th Fibonacci number
    fib_29 = fibonacci_sequence(29)[-1]
    # Check if the decimal integer is divisible by the 29th Fibonacci number
    return (num % fib_29) == 0
def fibonacci_sequence(n):
    # Initialize the first two Fibonacci numbers
    a = 0
    b = 1
    # Generate the rest of the Fibonacci sequence
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return [a, b]
