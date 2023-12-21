
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    decimal_int = int(binary_repr, 2)
    # Calculate the 77th Fibonacci number
    fib_77 = fibonacci(76)
    # Check if the decimal integer is divisible by the 77th Fibonacci number
    return decimal_int % fib_77 == 0
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
