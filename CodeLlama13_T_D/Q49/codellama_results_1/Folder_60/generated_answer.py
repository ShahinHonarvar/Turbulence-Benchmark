
def if_decimal_is_divisible(binary):
    # Convert the binary string to an integer
    n = int(binary, 2)
    
    # Calculate the Fibonacci sequence up to the 108th number
    fib = [0] * (n + 1)
    for i in range(n):
        if i < 2:
            fib[i] = i
        else:
            fib[i] = fib[i - 1] + fib[i - 2]
    
    # Check if the decimal integer is divisible by the 108th number
    return n % fib[107] == 0
