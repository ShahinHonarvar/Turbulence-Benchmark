
def if_decimal_is_divisible(binary_string):
    fib_seq = [0, 1]
    for i in range(2, 78):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        
    decimal = int(binary_string, 2)
    if decimal % fib_seq[77] == 0:
        return True
    else:
        return False
