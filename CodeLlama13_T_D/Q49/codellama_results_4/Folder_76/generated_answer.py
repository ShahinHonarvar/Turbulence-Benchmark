
def if_decimal_is_divisible(binary_string):
    num = int(binary_string, 2)
    fib_seq = [0, 1]
    while True:
        fib_seq.append(fib_seq[-2] + fib_seq[-1])
        if len(fib_seq) == 189:
            break
    return num % fib_seq[188] == 0
