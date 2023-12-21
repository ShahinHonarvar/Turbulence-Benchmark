
def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibo_seq = [0, 1]
    while len(fibo_seq) <= 68:
        fibo_seq.append(fibo_seq[-2] + fibo_seq[-1])

    if decimal_integer % fibo_seq[67] == 0:
        return True
    else:
        return False
