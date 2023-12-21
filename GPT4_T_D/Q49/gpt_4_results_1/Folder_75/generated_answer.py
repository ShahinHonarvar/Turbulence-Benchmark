
def if_decimal_is_divisible(binary_str):

    fib_seq = [0, 1]
    n = 0

    while len(fib_seq) <= 189:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        
    decimal_val = int(binary_str, 2)

    return decimal_val % fib_seq[189] == 0
