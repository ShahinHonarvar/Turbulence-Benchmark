
def if_decimal_is_divisible(binary_num):
    num = int(binary_num, 2)
    fib_seq = [0, 1]
    while len(fib_seq) <= 178:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return num % fib_seq[178] == 0
