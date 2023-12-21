
def if_decimal_is_divisible(binary_rep):
    # Convert the binary representation to an integer
    decimal_int = int(binary_rep, 2)
    # Calculate the 46th number in the Fibonacci sequence
    fib_seq = [0, 1]
    while len(fib_seq) < 46:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    # Check if the decimal integer is divisible by the 46th Fibonacci number
    return decimal_int % fib_seq[45] == 0
