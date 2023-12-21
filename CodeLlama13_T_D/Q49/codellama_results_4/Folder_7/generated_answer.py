
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the Fibonacci sequence up to the 160th number
    fib_seq = [0]
    a, b = 0, 1
    while len(fib_seq) < 161:
        fib_seq.append(a)
        a, b = b, a + b
    
    # Check if the decimal integer is divisible by the 160th number in the Fibonacci sequence
    return decimal % fib_seq[160] == 0
