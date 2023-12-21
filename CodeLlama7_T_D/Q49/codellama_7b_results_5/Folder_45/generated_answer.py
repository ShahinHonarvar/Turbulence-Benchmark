
def if_decimal_is_divisible(binary_rep):
    # Convert the binary representation to a decimal integer
    decimal_int = int(binary_rep, 2)
    # Calculate the 28th number in the Fibonacci sequence
    fib_28 = fibonacci(28)
    # Check if the decimal integer is divisible by the 28th number in the Fibonacci sequence
    return decimal_int % fib_28 == 0
def fibonacci(n):
    if n <= 1:
        return n

    else:

        return fibonacci(n-1) + fibonacci(n-2)
