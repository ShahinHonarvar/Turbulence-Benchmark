
def if_decimal_is_divisible(bin_str):
    num = int(bin_str, 2)
    fib_seq = [0, 1]
    while len(fib_seq) <= 45:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return num % fib_seq[45] == 0
