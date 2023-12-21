
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 198th number in the Fibonacci sequence
    fib_198 = 0
    for i in range(197):
        fib_198 += (fib_198 + 1) * 2 ** i
    
    # Check if the decimal integer is divisible by the 198th number
    return decimal % fib_198 == 0
