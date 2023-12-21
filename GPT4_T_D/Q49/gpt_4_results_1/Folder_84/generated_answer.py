
def if_decimal_is_divisible(binary_string):
    fib_seq = [0, 1]
    while len(fib_seq) < 197:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    num = int(binary_string, 2)
    if num % fib_seq[196] == 0:
        return True
    else:
        return False
