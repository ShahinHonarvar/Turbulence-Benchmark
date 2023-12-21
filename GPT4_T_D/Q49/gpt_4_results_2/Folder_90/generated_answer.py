
def if_decimal_is_divisible(bin_string):
    fib_seq = [0, 1]
    for i in range(2, 177):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])

    decimal_num = int(bin_string, 2)
    if(decimal_num % fib_seq[176] == 0):
        return True
    else:
        return False
