
def if_decimal_is_divisible(binary_string):
    # Convert the binary representation string to an integer
    decimal = int(binary_string, 2)
    
    # Find the index of the seventh Fibonacci number (0-based indexing)
    fib7_index = 6
    
    # Find the seventh Fibonacci number using a recursive formula
    def fib(n):
        if n <= 1:
            return n
        else:
            return fib(n - 1) + fib(n - 2)
    
    fib7 = fib(fib7_index)
    
    # Check if the decimal integer is divisible by the seventh Fibonacci number
    if decimal % fib7 == 0:
        return True
    else:
        return False
