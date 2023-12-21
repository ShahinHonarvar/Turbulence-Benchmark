
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    decimal = int(binary_repr, 2)
    
    # Calculate the Fibonacci sequence until we reach 99
    fib = [0]
    while len(fib) < 99:
        fib.append(fib[-1] + fib[-2])
    
    # Check if the decimal is divisible by any of the numbers in the Fibonacci sequence
    for i in range(len(fib)):
        if decimal % fib[i] == 0:
            return True
    
    # If none of the numbers in the Fibonacci sequence divide the decimal, return False
    return False
