
def if_decimal_is_divisible(binary_rep):
    # Convert the binary representation to an integer
    decimal_int = int(binary_rep, 2)
    # Compute the Fibonacci sequence up to the 19th term
    fib_seq = [0, 1]
    for i in range(2, 19):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    # Check if the decimal integer is divisible by the 19th term of the Fibonacci sequence
    return decimal_int % fib_seq[18] == 0
