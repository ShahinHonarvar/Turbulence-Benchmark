
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 199th number in the Fibonacci sequence
    fib_199 = 0
    for i in range(198):
        fib_199 += fib[i]
        
    # Check if the decimal is divisible by the 199th number
    return decimal % fib_199 == 0
