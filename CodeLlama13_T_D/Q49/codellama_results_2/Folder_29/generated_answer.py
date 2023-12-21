
def if_decimal_is_divisible(binary_string):
    # Convert the binary string to an integer
    decimal = int(binary_string, 2)
    
    # Calculate the 117th number that occurs in the Fibonacci sequence
    fib_seq = [0]
    for i in range(116):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    # Check if the decimal integer is divisible by the 117th number in the Fibonacci sequence
    return decimal % fib_seq[116] == 0
