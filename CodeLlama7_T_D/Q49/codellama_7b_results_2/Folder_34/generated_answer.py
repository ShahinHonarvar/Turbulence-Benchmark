
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    decimal_int = int(binary_repr, 2)
    # Calculate the 24th number that occurs in the Fibonacci sequence
    fib_24 = fibonacci(24)
    # Check if the decimal integer is divisible by the 24th Fibonacci number
    return (decimal_int % fib_24 == 0)
def fibonacci(n):
    if n <= 1:
        return n

    else:

        return fibonacci(n - 1) + fibonacci(n - 2)
