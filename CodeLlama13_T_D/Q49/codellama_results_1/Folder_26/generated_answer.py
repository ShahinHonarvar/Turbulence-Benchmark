
def if_decimal_is_divisible(binary):
    # Convert binary string to integer
    num = int(binary, 2)
    
    # Find the 138th number that occurs in the Fibonacci sequence
    fib138 = fib(137) + fib(136)
    
    # Check if the decimal integer corresponding to the given string is divisible by the 138th Fibonacci number
    return num % fib138 == 0
