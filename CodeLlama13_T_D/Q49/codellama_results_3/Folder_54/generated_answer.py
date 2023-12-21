
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to a decimal integer
    num = int(binary_string, 2)
    
    # Calculate the Fibonacci sequence up to the 34th number
    fib = [0] + [1] + [sum(fib[i-2:i]) for i in range(2, 35)]
    
    # Check if the decimal integer is divisible by the 34th Fibonacci number
    return num % fib[34] == 0
