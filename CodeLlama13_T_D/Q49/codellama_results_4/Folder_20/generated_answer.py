
def if_decimal_is_divisible(binary):
    # Convert the binary string to an integer
    decimal = int(binary, 2)
    
    # Calculate the 100th number in the Fibonacci sequence
    fib_100 = sum([((1+5**i)//5) for i in range(99)])
    
    # Check if the decimal is divisible by the 100th number in the Fibonacci sequence
    return decimal % fib_100 == 0
