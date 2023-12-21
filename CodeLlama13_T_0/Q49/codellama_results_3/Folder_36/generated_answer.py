
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 150th number in the Fibonacci sequence
    fib_150 = 0
    a, b = 0, 1
    for i in range(149):
        fib_150 += a
        a, b = b, a + b
    
    # Check if the decimal integer is divisible by the 150th number in the Fibonacci sequence
    return decimal % fib_150 == 0
