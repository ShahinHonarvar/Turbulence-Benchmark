
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 85th number in the Fibonacci sequence
    fib85 = 0
    a, b = 0, 1
    for i in range(84):
        fib85 = a + b
        a, b = b, fib85
    
    # Check if the decimal is divisible by the 85th Fibonacci number
    return decimal % fib85 == 0
