
def if_decimal_is_divisible(binary):
    fib_seq = [0, 1]
    while len(fib_seq) < 165:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    decimal = int(binary, 2)
    desired_fib_num = fib_seq[164]

    return decimal % desired_fib_num == 0
