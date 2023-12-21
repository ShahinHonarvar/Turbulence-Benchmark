
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal number
    decimal = int(binary_string, 2)
    
    # Calculate the Fibonacci sequence up to 54th number
    fib = [0] + [a + b for a, b in zip([0, 1], fib[1:])]
    
    # Check if the decimal number is divisible by the 54th number of the Fibonacci sequence
    return True if decimal % fib[53] == 0 else False
