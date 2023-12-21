
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 134th number in the Fibonacci sequence
    fib_134 = 0
    a, b = 0, 1
    for i in range(134):
        fib_134 = a + b
        a, b = b, fib_134
    
    # Check if the decimal integer is divisible by the 134th Fibonacci number
    return decimal % fib_134 == 0
