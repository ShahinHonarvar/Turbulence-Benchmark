
def if_decimal_is_divisible(binary):
    binary_to_decimal = int(binary, 2)
     
    fib_seq = [0, 1]
    for i in range(2, 78):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])

    fib_78th = fib_seq[-1]
    
    if binary_to_decimal % fib_78th == 0:
        return True
    else:
        return False
