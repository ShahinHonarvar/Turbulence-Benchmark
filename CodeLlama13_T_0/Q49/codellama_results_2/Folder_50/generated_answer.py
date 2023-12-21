
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 119th number in the Fibonacci sequence
    fib_119 = 0
    for i in range(118):
        fib_119 += fib[i]
        
    # Check if the decimal is divisible by the 119th number
    return decimal % fib_119 == 0
