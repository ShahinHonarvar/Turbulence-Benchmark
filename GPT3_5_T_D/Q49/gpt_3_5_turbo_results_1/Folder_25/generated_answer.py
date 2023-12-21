
def if_decimal_is_divisible(binary_num):
    fib_seq = [0, 1]
    while len(fib_seq) < 20:
        next_num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_num)
    
    decimal_num = int(binary_num, 2)
    if decimal_num % fib_seq[18] == 0:
        return True
    else:
        return False
