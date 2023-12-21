
def if_decimal_is_divisible(binary_string):
    # convert the binary string to an integer
    decimal_int = int(binary_string, 2)
    # initialize the Fibonacci sequence with the first two numbers
    fib = [0, 1]
    # loop through the Fibonacci sequence until we find the 84th number
    for i in range(2, 85):
        # add the previous two numbers to get the next number in the sequence
        fib.append(fib[-2] + fib[-1])
    # check if the decimal integer is divisible by the 84th Fibonacci number
    return decimal_int % fib[83] == 0
