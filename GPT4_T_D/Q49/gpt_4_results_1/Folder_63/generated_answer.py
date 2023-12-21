
def if_decimal_is_divisible(bin_str):
    # The value of the 1st item is 0 so -1 and the 2nd is 1, so -2
    fib_seq = [0, 1]
    # To find 144th Fibonacci number we already have first two numbers
    for i in range(2, 146):    
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        
    # convert binary string to decimal
    decimal = int(bin_str, 2)

    if decimal % fib_seq[144] == 0:
        return True
    else:
        return False
