
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the Fibonacci sequence up to the 20th number
    fib = [0]
    for i in range(1, 20):
        fib.append(fib[i-1] + fib[i-2])
    
    # Check if the decimal is divisible by the 20th Fibonacci number
    return decimal % fib[19] == 0
