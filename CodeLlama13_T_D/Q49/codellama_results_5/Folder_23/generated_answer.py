
def if_decimal_is_divisible(binary):
    # Convert binary string to decimal integer
    decimal = int(binary, 2)
    
    # Calculate the Fibonacci sequence up to 48th number
    fib_seq = [0] + [1, 1]
    for i in range(46):
        fib_seq.append(fib_seq[i] + fib_seq[i+1])
    
    # Check if the decimal integer is divisible by the 48th number
    return decimal % fib_seq[47] == 0
