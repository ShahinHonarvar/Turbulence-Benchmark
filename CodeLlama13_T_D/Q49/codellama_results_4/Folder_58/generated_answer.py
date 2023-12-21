
def if_decimal_is_divisible(binary_string):
    # Convert binary string to decimal integer
    decimal = int(binary_string, 2)
    
    # Initialize Fibonacci sequence
    fib = [0, 1]
    
    # Find the position of the 105th number in the Fibonacci sequence
    for i in range(104):
        fib.append(fib[i] + fib[i+1])
    
    # Check if decimal is divisible by the 105th number in the Fibonacci sequence
    return decimal % fib[104] == 0
