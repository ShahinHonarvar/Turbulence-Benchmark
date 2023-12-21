
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Get the Fibonacci sequence up to the 187th number
    fib_seq = [0] + [a + b for a, b in zip(fib_seq, fib_seq[1:])]
    
    # Check if the decimal is divisible by the 187th Fibonacci number
    return decimal % fib_seq[186] == 0
