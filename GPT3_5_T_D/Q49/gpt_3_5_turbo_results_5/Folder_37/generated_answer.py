
def if_decimal_is_divisible(bin_num):
    fib_seq = [0, 1]
    while len(fib_seq) < 47:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    decimal_num = int(bin_num, 2)
    return decimal_num % fib_seq[45] == 0
