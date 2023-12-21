
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 19th number in the Fibonacci sequence
    fib_19 = 346_264_008_152_789_673
    
    # Check if the decimal is divisible by the 19th number in the Fibonacci sequence
    return decimal % fib_19 == 0
