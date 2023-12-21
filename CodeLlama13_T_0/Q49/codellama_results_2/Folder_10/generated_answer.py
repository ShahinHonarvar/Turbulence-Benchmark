
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 88th number in the Fibonacci sequence
    fib88 = 1346269
    
    # Check if the decimal is divisible by the 88th number
    return decimal % fib88 == 0
