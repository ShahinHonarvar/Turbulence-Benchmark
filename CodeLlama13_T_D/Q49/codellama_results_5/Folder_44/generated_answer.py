
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    decimal = int(binary_string, 2)
    
    # Calculate the 159th Fibonacci number
    fib_159 = fibonacci(159)
    
    # Check if the decimal is divisible by the 159th Fibonacci number
    return decimal % fib_159 == 0

# Define a function to calculate the nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
