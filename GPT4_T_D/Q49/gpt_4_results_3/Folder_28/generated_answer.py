
def if_decimal_is_divisible(binary_string):
    fib_seq = [0, 1]
    num = int(binary_string, 2)
    i = 2
    
    while len(fib_seq) < 104:
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
        i += 1
    
    if num % fib_seq[-1] == 0:
        return True
    else:
        return False
