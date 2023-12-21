
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 115th number in the Fibonacci sequence
    fib_115 = 0
    for i in range(115):
        fib_115 += (fib_114 * fib_113) % 10
    
    # Check if the decimal is divisible by the 115th number
    return decimal % fib_115 == 0
