
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # Check if the decimal integer is divisible by the 27th Fibonacci number
    fib_27 = fibonacci(27)
    return (decimal_int % fib_27) == 0
def fibonacci(n):
    # Base case
    if n <= 1:
        return n

    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
