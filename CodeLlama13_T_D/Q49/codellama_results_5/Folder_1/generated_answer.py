
def if_decimal_is_divisible(binary):
    # Convert the binary string to an integer
    num = int(binary, 2)
    
    # Initialize a list to store the Fibonacci sequence
    fib = [0]
    
    # Calculate the first 90 numbers of the Fibonacci sequence
    for i in range(1, 90):
        fib.append((fib[i-1] + fib[-1]) % (2**32 - 1))
    
    # Check if the decimal integer is divisible by any of the numbers in the Fibonacci sequence
    for i in range(90):
        if num % fib[i] == 0:
            return True
    
    # If none of the numbers in the Fibonacci sequence divide the decimal integer, return false
    return False
