
def if_decimal_is_divisible(binary_string):
    # Calculate the decimal value of the binary string
    decimal_value = 0
    for digit in binary_string:
        decimal_value *= 2
        if digit == '1':
            decimal_value += 1
    
    # Calculate the Fibonacci sequence up to 104th number
    fib_seq = [0]
    while len(fib_seq) < 105:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    # Check if the decimal value is divisible by the 104th number in the Fibonacci sequence
    return decimal_value % fib_seq[104] == 0
