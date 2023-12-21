
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 174th number in the Fibonacci sequence
    fib_174 = 0
    a, b = 0, 1
    for i in range(173):
        a, b = b, a + b
    fib_174 = b
    
    # Check if the decimal integer is divisible by the 174th number
    return decimal % fib_174 == 0
