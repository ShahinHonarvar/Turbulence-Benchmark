
def if_decimal_is_divisible(binary_rep):
    # Convert the binary representation to a decimal integer
    decimal_int = int(binary_rep, 2)
    # Find the index of the 189th occurrence of 0 in the Fibonacci sequence
    fib_seq = [0, 1]
    for i in range(1, len(fib_seq)):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i])
    index_189 = next((i for i, x in enumerate(fib_seq) if x == 0), None)
    # Check if the decimal integer is divisible by the 189th Fibonacci number
    return decimal_int % fib_seq[index_189 + 188] == 0
