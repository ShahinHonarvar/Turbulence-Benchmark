
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal_integer = int(binary_string, 2)
    # Calculate the 77th Fibonacci number
    fibonacci_77 = calculate_fibonacci(76)
    # Check if the decimal integer is divisible by the 77th Fibonacci number
    return decimal_integer % fibonacci_77 == 0
def calculate_fibonacci(n):
    # Initialize the first two Fibonacci numbers
    a = 0
    b = 1
    # Calculate the nth Fibonacci number
    for i in range(n-1):
        c = a + b
        a = b
        b = c
    return b
