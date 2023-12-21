
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 14th number in the Fibonacci sequence
    fib14 = 3 * (2 ** 14) + 1
    
    # Check if the decimal is divisible by the 14th number in the Fibonacci sequence
    return decimal % fib14 == 0
