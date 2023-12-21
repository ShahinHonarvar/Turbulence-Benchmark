
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 160th number in the Fibonacci sequence
    fib_160 = (((1 + 5 ** 0.5) / 2) ** 160 - ((1 - 5 ** 0.5) / 2) ** 160) / 5 ** 0.5
    
    # Check if the decimal integer is divisible by the 160th number in the Fibonacci sequence
    return decimal % fib_160 == 0
