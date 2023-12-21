
def if_decimal_is_divisible(binary_str):
    num = int(binary_str, 2)
    fib_seq = [0, 1]
    while len(fib_seq) <= 168:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    if num % fib_seq[168] == 0:
        return True
    else:
        return False
