
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    num = int(binary_string, 2)
    
    # Calculate the 175th number that occurs in the Fibonacci sequence
    fib175 = 0
    a, b = 0, 1
    for i in range(175):
        a, b = b, a + b
    
    # Check if num is divisible by fib175
    if num % fib175 == 0:
        return True
    else:
        return False
