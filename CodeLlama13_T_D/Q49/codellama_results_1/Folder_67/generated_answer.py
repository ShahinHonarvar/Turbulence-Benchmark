
def if_decimal_is_divisible(binary):
    # Convert the binary representation string to a decimal integer
    decimal = int(binary, 2)
    
    # Calculate the 107th number in the Fibonacci sequence
    fib_107 = fibonacci(107)
    
    # Check if the decimal integer is divisible by the 107th Fibonacci number
    if decimal % fib_107 == 0:
        return True
    else:
        return False
