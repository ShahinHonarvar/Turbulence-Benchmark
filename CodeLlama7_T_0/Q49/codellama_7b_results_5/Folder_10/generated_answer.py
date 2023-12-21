
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 88th Fibonacci number
    fib_88 = fibonacci(88)
    # Check if the decimal integer is divisible by the 88th Fibonacci number
    return (decimal_integer % fib_88 == 0)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
