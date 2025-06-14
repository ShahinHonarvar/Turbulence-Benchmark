
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 139th number in the Fibonacci sequence
    fib_139 = 0
    a, b = 0, 1
    for i in range(138):
        fib_139 = a + b
        a, b = b, fib_139
    
    # Check if the decimal integer is divisible by the 139th number in the Fibonacci sequence
    return decimal % fib_139 == 0
