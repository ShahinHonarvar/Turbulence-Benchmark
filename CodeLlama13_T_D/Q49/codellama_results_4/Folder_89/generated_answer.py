
def if_decimal_is_divisible(binary_string):
    # Convert binary string to integer
    decimal = int(binary_string, 2)
    
    # Compute the 126th number that occurs in the Fibonacci sequence
    fib_126 = 0
    a, b = 0, 1
    for i in range(125):
        fib_126 = a + b
        a, b = b, fib_126
    
    # Check if the decimal integer is divisible by the 126th Fibonacci number
    if decimal % fib_126 == 0:
        return True
    else:
        return False
