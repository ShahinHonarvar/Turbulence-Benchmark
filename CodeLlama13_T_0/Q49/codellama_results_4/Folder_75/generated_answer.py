
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 189th number in the Fibonacci sequence
    fib_189 = 0
    a, b = 0, 1
    for i in range(189):
        fib_189 += a
        a, b = b, a + b
    
    # Check if the decimal integer is divisible by the 189th number
    return decimal % fib_189 == 0
