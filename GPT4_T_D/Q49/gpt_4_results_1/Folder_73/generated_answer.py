
def if_decimal_is_divisible(binary_num):
    fib_seq = [0, 1]
    while len(fib_seq) < 165:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    num_164th_fib = fib_seq[-1]
    
    num = int(binary_num, 2)
    return num % num_164th_fib == 0
