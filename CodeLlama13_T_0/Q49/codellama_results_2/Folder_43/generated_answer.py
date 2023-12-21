
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 77th number in the Fibonacci sequence
    fib_77 = 1346269
    
    # Check if the decimal is divisible by the 77th number
    return decimal % fib_77 == 0
