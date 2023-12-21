
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 127th number in the Fibonacci sequence
    fib_127 = 0
    a, b = 0, 1
    for i in range(126):
        fib_127 = a + b
        a, b = b, fib_127
    
    # Check if the decimal integer is divisible by the 127th number
    return decimal % fib_127 == 0
