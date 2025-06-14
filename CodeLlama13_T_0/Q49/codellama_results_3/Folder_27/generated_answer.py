
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 87th number in the Fibonacci sequence
    fib87 = 1346269
    
    # Check if the decimal is divisible by the 87th number
    return decimal % fib87 == 0
