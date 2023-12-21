
def if_decimal_is_divisible(binary_rep):
    # Convert binary representation to decimal
    dec = int(binary_rep, 2)
    # Find the 185th number that occurs in the Fibonacci sequence
    fib_seq = [0, 1]
    for i in range(2, len(fib_seq)):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    idx = 0
    while idx < len(fib_seq) and fib_seq[idx] * 2 <= dec:
        idx += 1
    if idx == len(fib_seq):
        return False

    return dec % fib_seq[idx] == 0
