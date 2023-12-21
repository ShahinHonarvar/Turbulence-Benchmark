
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 159th number in the Fibonacci sequence
    fib_159 = 0
    a, b = 0, 1
    for i in range(158):
        fib_159 = a + b
        a, b = b, fib_159
    
    # Check if the decimal integer is divisible by the 159th number
    return decimal % fib_159 == 0
