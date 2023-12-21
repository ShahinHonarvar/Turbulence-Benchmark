
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 17th number in the Fibonacci sequence
    fib17 = 0
    for i in range(17):
        fib17 += fib[i]
    
    # Check if the decimal is divisible by the 17th number in the Fibonacci sequence
    return decimal % fib17 == 0
