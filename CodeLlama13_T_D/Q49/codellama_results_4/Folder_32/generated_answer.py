
def if_decimal_is_divisible(binary):
    # Convert binary string to decimal integer
    dec = int(binary, 2)
    
    # Find the 178th Fibonacci number
    fib = [0, 1]
    for i in range(177):
        fib.append(fib[i] + fib[i+1])
        
    # Check if decimal is divisible by the 178th Fibonacci number
    return dec % fib[177] == 0
