
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 54th number in the Fibonacci sequence
    fib_54 = 0
    for i in range(53):
        fib_54 += (1 << i) * (fib_54 % 2 == 0)
    
    # Check if the decimal is divisible by the 54th number
    return decimal % fib_54 == 0
