
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 154th number in the Fibonacci sequence
    fib_154 = 0
    a, b = 0, 1
    for i in range(153):
        fib_154 = a + b
        a, b = b, fib_154
    
    # Check if the decimal integer is divisible by the 154th number in the Fibonacci sequence
    return decimal % fib_154 == 0
