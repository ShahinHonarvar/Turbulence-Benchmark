
def if_decimal_is_divisible(binary):
    # Convert the binary string to an integer
    num = int(binary, 2)
    
    # Calculate the Fibonacci sequence up to the 100th number
    fib = [0] + [1, 1] + [sum(fib[i-2:i]) for i in range(2, 101)]
    
    # Check if the decimal integer is divisible by the 100th Fibonacci number
    return num % fib[99] == 0
