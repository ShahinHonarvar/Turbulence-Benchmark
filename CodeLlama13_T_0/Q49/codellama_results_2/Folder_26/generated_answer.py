
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 138th number in the Fibonacci sequence
    fib_138 = 0
    a, b = 0, 1
    for i in range(137):
        fib_138 = a + b
        a, b = b, fib_138
    
    # Check if the decimal integer is divisible by the 138th Fibonacci number
    return decimal % fib_138 == 0
