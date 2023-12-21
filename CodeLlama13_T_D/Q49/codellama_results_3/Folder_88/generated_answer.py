
def if_decimal_is_divisible(binary):
    # Convert the binary string to a decimal integer
    dec = int(binary, 2)
    
    # Calculate the Fibonacci sequence up to 49
    fib = [0, 1] + [fib[i-1] + fib[i-2] for i in range(2, 49)]
    
    # Check if dec is divisible by the 49th number of Fibonacci sequence
    return (dec % fib[48]) == 0
