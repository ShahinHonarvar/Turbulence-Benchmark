
def if_decimal_is_divisible(binary_repr):
    # Convert the binary representation string to an integer
    decimal = int(binary_repr, 2)
    
    # Calculate the Fibonacci sequence up to 128th number
    fib_seq = [0] + [x for x in [0, 1]] + [sum(fib_seq[i-2:i]) for i in range(2, 129)]
    
    # Return true if the decimal integer is divisible by the 128th number
    return decimal % fib_seq[127] == 0
