
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Compute the Fibonacci sequence up to the 74th number
    fib = [0] * (75)
    for i in range(1, len(fib)):
        fib[i] = fib[i-1] + fib[i-2]
    
    # Check if the decimal integer is divisible by the 74th number
    return decimal % fib[74] == 0
