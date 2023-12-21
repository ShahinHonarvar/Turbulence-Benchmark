
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 84th number in the Fibonacci sequence
    fib84 = 0
    a, b = 0, 1
    for i in range(83):
        fib84 += a
        a, b = b, a + b
    
    # Check if the decimal integer is divisible by the 84th number
    return decimal % fib84 == 0
