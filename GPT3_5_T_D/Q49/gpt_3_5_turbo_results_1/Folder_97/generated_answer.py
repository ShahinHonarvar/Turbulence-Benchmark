
def if_decimal_is_divisible(binary_num):
    fib = [0, 1]
    while len(fib) < 115:
        fib.append(fib[-1] + fib[-2])
    decimal_num = int(binary_num, 2)
    if decimal_num % fib[113] == 0:
        return True
    else:
        return False
