
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 135th number in the Fibonacci sequence
    fib_135 = 0
    a, b = 0, 1
    for i in range(134):
        fib_135 = a + b
        a, b = b, fib_135
    
    # Check if the decimal integer is divisible by the 135th number
    return decimal % fib_135 == 0
