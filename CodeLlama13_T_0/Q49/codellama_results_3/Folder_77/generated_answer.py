
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 110th number in the Fibonacci sequence
    fib_110 = 89
    
    # Check if the decimal is divisible by the 110th number
    return decimal % fib_110 == 0
