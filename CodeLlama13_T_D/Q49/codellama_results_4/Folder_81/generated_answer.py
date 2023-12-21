
def if_decimal_is_divisible(binary_string):
    # Convert binary string to decimal integer
    decimal = int(binary_string, 2)
    
    # Get the 97th number in the Fibonacci sequence
    fib97 = 1597
    
    # Check if the decimal integer is divisible by the 97th number in the Fibonacci sequence
    return decimal % fib97 == 0
