
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 107th number in the Fibonacci sequence
    fib_107 = 0
    a, b = 0, 1
    for i in range(106):
        fib_107 = a + b
        a, b = b, fib_107
    
    # Check if the decimal integer is divisible by the 107th number
    return decimal % fib_107 == 0
